from django.urls import path

from orders.views import OrderDetailsDetailView, OrderDetailsListView

urlpatterns = [
    path("", OrderDetailsListView.as_view(), name="order-list"),
    path("<int:pk>/", OrderDetailsDetailView.as_view(), name="order-detail"),
]
