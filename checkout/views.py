import os

import stripe
from datetime import datetime

from django.contrib import auth, messages
from django.db import Error as DatabaseError
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import FormView
from django.views import View
from django.forms import model_to_dict
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, reverse

from basket.contexts import basket_context
from checkout.forms import ShippingForm
from checkout.models import ShippingAddress, OrderDetails, OrderItems
from products.models import Product


class ShippingFormView(LoginRequiredMixin, FormView):
    """View for ShippingAddress form."""
    template_name = "shipping.html"
    form_class = ShippingForm
    success_url = reverse_lazy('payment')

    def get_initial(self):
        """Pre-populate form with last updated shipping address."""
        initial = super().get_initial()
        # Populate form with the last updated shipping address
        shipping_address_queryset = ShippingAddress.objects.filter(
            user=self.request.user).order_by("-updated").first()
        if shipping_address_queryset is not None:
            # Create dict from model data
            initial = model_to_dict(shipping_address_queryset)
        return initial

    def form_valid(self, form):
        """Create or update ShippingAddress database instance.

        If there is an existing ( and equal) shipping address then use that.
        If new form details, update a previous(unused) address or create new instance.
        """
        form.instance.user = self.request.user
        try:
            unused_address = ShippingAddress.objects.filter(
                user=self.request.user, orderdetails=None).order_by("-updated").first()
            if unused_address:
                form.instance.id = unused_address.id
                form.instance.created = unused_address.created
        except ShippingAddress.DoesNotExist:
            pass
        form.save()
        return super(ShippingFormView, self).form_valid(form)


class PaymentView(View):
    """View for Stripe Checkout payment."""
    GENERIC_STRIPE_ERROR = "Stripe Service temporarily unavailable, please try again later."
    GENERIC_ORDER_CONTACT_ERROR = "There was an error placing your order, please try again later or contact us for assistance."

    def get(self, request, order_id=None):
        """Handle the GET request to the PaymentView

        - Get the stripe API key from the environmental variables.
        - Resume payment of an existing order if order_id supplied else create new payment session.
        """
        stripe.api_key = os.environ.get("STRIPE_KEY")
        if order_id is not None:
            return self.existing_order_payment(request, order_id)
        else:
            return self.new_order_payment(request)

    def build_line_item(self, order_item, product):
        """Create standardised dict object required for Stripe Checkout session."""
        try:
            price = order_item.price
        except AttributeError:
            price = product.price

        return {
            "price_data": {
                "currency": "gbp",
                "product_data": {
                    "name": product.name
                },
                # Decimal('10.00') -> "1000"
                "unit_amount": str(price).replace(".", ""),
            },
            "quantity": order_item.quantity
        }

    def create_stripe_checkout_session(self, request, line_items):
        """Use Stripe API to create Stripe Checkout session."""
        try:
            stripe_session = stripe.checkout.Session.create(
                line_items=line_items,
                mode="payment",
                success_url=request.build_absolute_uri(
                    reverse("payment-success")),
                cancel_url=request.build_absolute_uri(
                    reverse("order-list"))
            )
        except stripe.error.StripeError as e:
            raise e
        return stripe_session

    def existing_order_payment(self, request, order_id):
        """Resume payment of an order that is pending payment.

        - Fetch the relevant order, scoped to the user.
        - Fetch the existing Checkout session.
        - Redirect to Checkout session if not expired.
        - If previous has expired, create a new Checkout session & redirect to its url.
        """
        try:
            order_details = OrderDetails.objects.filter(
                user=request.user).get(id=order_id)
        except OrderDetails.DoesNotExist:
            messages.error(
                request, "Your order could not be found, please try again.")
            return redirect("order-list")
        # Stripe Checkout sessions expire after 24 hours, create new (assume expired as safe default)
        stripe_session_expiry = 0
        if order_details.stripe_id is True:
            try:
                stripe_session = stripe.checkout.Session.retrieve(
                    order_details.stripe_id)
                stripe_session_expiry = stripe_session.expires_at
                if stripe_session["status"] == "complete":
                    order_details.payment_confirmed = True
                    order_details.save()
                    messages.success(
                        request, "Your payment has been confirmed.")
                    return redirect("order-list")
            except(stripe.error.StripeError, AttributeError, DatabaseError):
                messages.error(
                    request, "There was an error in processing your order, please try again.")
            return redirect("order-list")
        if order_details.stripe_id is False or stripe_session_expiry < datetime.now().timestamp():
            order_items = order_details.orderitems_set.all()
            products_list = [order.product for order in order_items]

            line_items = []
            for product in products_list:
                for order_item in order_items:
                    if order_item.product_id == product.id:
                        line_items.append(self.build_line_item(
                            order_item, product))

            if line_items:
                try:
                    stripe_session = self.create_stripe_checkout_session(
                        request, line_items)
                except stripe.error.StripeError:
                    messages.error(
                        request, self.GENERIC_STRIPE_ERROR)
                    return redirect("order-list")
                order_details.stripe_id = stripe_session.id
                order_details.save()
        else:
            # Stripe Checkout session still valid, continue on their site
            # Mark the order as updated to be used in PaymentSuccess
            order_details.save()
            return redirect(stripe_session.url)

        try:
            return redirect(stripe_session.url)
        except NameError:
            messages.error(request, self.GENERIC_ORDER_CONTACT_ERROR)
            return redirect("order-list")

    def new_order_payment(self, request):
        """Create order and Stripe Checkout session.

        - Get the item details from the basket.
        - Get the relevant ShippingAddress from the user.
        - Call stock check on items in basket.
        - Create order item(with price frozen at current stock price).
        - Increase total order price/order quantity and decrease available stock quantity accordingly.
        - Build a list of line items to be used in the Checkout session.
        - Empty the basket.
        - Redirect to Checkout session url.
        """
        # Create Checkout session with line_items from basket
        basket_details = basket_context(request)
        basket_items = basket_details["basket"]

        try:
            shipping_address = ShippingAddress.objects.filter(
                user=request.user).order_by("-updated").first()
        except ShippingAddress.DoesNotExist:
            messages.error(
                request, "Please enter shipping address information.")
            return redirect("shipping-form")

        try:
            order_details = OrderDetails.objects.create(
                user=request.user, shipping_address=shipping_address)
        except DatabaseError:
            messages.error(request, self.GENERIC_ORDER_CONTACT_ERROR)
            return redirect("basket")

        product_item_ids = [item["id"] for item in basket_items]
        products = Product.objects.filter(id__in=product_item_ids)

        line_items = []
        for product in products:
            for item in basket_items:
                if item["id"] == product.id:
                    if product.sufficient_stock(item["quantity"]):
                        try:
                            order_item = OrderItems.objects.create(
                                order_details=order_details,
                                product=product,
                                quantity=item["quantity"],
                                price=product.price
                            )
                        except DatabaseError:
                            messages.error(
                                request, self.GENERIC_ORDER_CONTACT_ERROR)
                            return redirect("basket")
                        if order_item is not None:
                            order_details.total_price += order_item.quantity * order_item.price
                            order_details.items_quantity += order_item.quantity
                            product.quantity -= order_item.quantity
                            product.save()
                            line_items.append(
                                self.build_line_item(order_item, product))
        # Write order to database in case stripe session creation fails
        try:
            order_details.save()
        except DatabaseError:
            messages.error(request, self.GENERIC_ORDER_CONTACT_ERROR)
            return redirect("basket")

        basket = request.session.get("basket", [])
        if basket:
            request.session["basket"] = []

        if line_items:
            try:
                stripe_session = self.create_stripe_checkout_session(
                    request, line_items)
            except stripe.error.StripeError:
                messages.error(request, self.GENERIC_STRIPE_ERROR)
                return redirect("order-list")

        # Update OrderDetails instance with new stripe session ID

        order_details.stripe_id = stripe_session.id
        try:
            order_details.save()
        except DatabaseError:
            messages.error(request, self.GENERIC_ORDER_CONTACT_ERROR)
            return redirect("basket")

        return redirect(stripe_session.url)


class PaymentSuccessView(View):
    """View for Payment Success."""

    def get(self, request):
        """Handle get request for PaymentSuccess

        - Get the user's latest updated order.
        - Retrieve the Checkout session to confirm if payment complete.
        - Mark the payment as complete in the order if Checkout complete.
        - Display success template if complete.
        - Display the user's orders if not complete.
        """
        order = OrderDetails.objects.filter(
            user=request.user).order_by("-updated").first()

        if order is not None:
            stripe.api_key = os.environ.get("STRIPE_KEY")

            try:
                stripe_session = stripe.checkout.Session.retrieve(
                    order.stripe_id)
            except stripe.error.StripeError:
                messages.error(
                    request, "Service temporarily unavailable, please try again later.")
                return redirect("order-list")

            if stripe_session["status"] == "complete":
                order.payment_confirmed = True
                order.save()
            else:
                messages.warning(
                    request, "Please check your order's payment status.")
                return redirect("order-list")

            return(render(request, "payment_success.html"))
