from checkout.forms import ShippingForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect


class ShippingFormView(LoginRequiredMixin, FormView):
    template_name = "shipping.html"
    form_class = ShippingForm
    success_url = reverse_lazy('payment')

    def form_valid(self, form):
        form = form.save(commit=False)
        form.user = self.request.user
        form.save()
        return redirect(self.get_success_url())


def payment_view(request):
    return render(request, "payment.html")
