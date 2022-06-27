from checkout.forms import ShippingForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import FormView
from django.forms import model_to_dict
from django.urls import reverse_lazy
from django.shortcuts import render

from checkout.models import ShippingAddress


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
            unused_address = ShippingAddress.objects.get(
                user=self.request.user, orderdetails=None)
            if unused_address:
                form.instance.id = unused_address.id
                form.instance.created = unused_address.created
        except ShippingAddress.DoesNotExist:
            pass
        form.save()
        return super(ShippingFormView, self).form_valid(form)


def payment_view(request):
    return render(request, "payment.html")
