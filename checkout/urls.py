from django.urls import path

from checkout.views import PaymentSuccessView, PaymentView, ShippingFormView

urlpatterns = [
    path(
        'shipping/',
        ShippingFormView.as_view(),
        name='shipping-form'),
    path(
        'payment/',
        PaymentView.as_view(),
        name="payment"),
    path(
        'payment/<int:order_id>/',
        PaymentView.as_view(),
        name="payment"),
    path(
        'payment/success/',
        PaymentSuccessView.as_view(),
        name="payment-success")]
