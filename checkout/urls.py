from django.urls import path
from checkout.views import ShippingFormView, PaymentFormView

urlpatterns = [
    path('shipping/', ShippingFormView.as_view(),
         name='shipping-form'),
    path('payment/', PaymentFormView.as_view(), name="payment")
]
