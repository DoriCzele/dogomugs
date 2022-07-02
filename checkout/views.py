import os
import stripe

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
    template_name = "shipping.html"
    form_class = ShippingForm
    success_url = reverse_lazy('payment')

    def get_initial(self):
        initial = super().get_initial()
        # Populate form with the last updated shipping address
        shipping_address_queryset = ShippingAddress.objects.filter(
            user=self.request.user).order_by("-updated").first()
        if shipping_address_queryset is not None:
            # Create dict from model data
            initial = model_to_dict(shipping_address_queryset)
        return initial

    def form_valid(self, form):
        form.instance.user = self.request.user
        # Need to handle existing shipping address being equal and having orderdetails
        # Update latest existing shipping address if not related to an order
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
    def get(self, request):

        basket_details = basket_context(request)
        basket_items = basket_details["basket"]
        line_items = []

        item_ids = [item["id"] for item in basket_items]
        products = Product.objects.filter(id__in=item_ids)
        shipping_address = ShippingAddress.objects.filter(
            user=request.user).order_by("-updated").first()

        order_details = OrderDetails.objects.create(
            user=request.user, shipping_address=shipping_address)

        for product in products:
            for item in basket_items:
                if item["id"] == product.id:
                    if product.sufficient_stock(item["quantity"]):
                        order_item = OrderItems.objects.create(
                            order_details=order_details,
                            product=product,
                            quantity=item["quantity"],
                            price=product.price,
                        )
                        if order_item is not None:
                            order_details.total_price += order_item.quantity * order_item.price
                            order_details.items_quantity += order_item.quantity
                            product.quantity -= order_item.quantity
                            product.save()
                            line_items.append({
                                "price_data": {
                                    "currency": "gbp",
                                    "product_data": {
                                        "name": product.name
                                    },
                                    # Decimal('10.00') -> "1000"
                                    "unit_amount": str(product.price).replace(".", ""),
                                },
                                "quantity": order_item.quantity
                            })
                    else:
                        return redirect(reverse("basket"))
        stripe.api_key = os.environ.get("STRIPE_KEY")

        if line_items:
            stripe_session = stripe.checkout.Session.create(
                line_items=line_items,
                mode="payment",
                success_url=request.build_absolute_uri(
                    reverse("payment-success")),
                cancel_url=request.build_absolute_uri(
                    reverse("basket"))
            )
        order_details.stripe_id = stripe_session.id
        order_details.save()

        basket = request.session.get("basket", [])
        if basket:
            request.session["basket"] = []

        return redirect(stripe_session.url)


class PaymentSuccessView(View):
    def get(self, request):
        order = OrderDetails.objects.filter(
            user=request.user).order_by("-updated").first()

        stripe.api_key = os.environ.get("STRIPE_KEY")
        stripe_session = stripe.checkout.Session.retrieve(order.stripe_id)

        if stripe_session["status"] == "complete":
            order.payment_confirmed = True
            order.save()
        else:
            # TODO: redirect to orders page (when created)
            return redirect("basket")

        return(render(request, "payment_success.html"))
