from django.urls import path
from checkout.views import ShippingFormView, payment_view

urlpatterns = [
    path('shipping/', ShippingFormView.as_view(),
         name='shipping-form'),
    path('payment/', payment_view, name="payment")
]
