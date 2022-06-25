from django.contrib import admin
from checkout.models import OrderDetails, OrderItems, ShippingAddress

admin.site.register(OrderDetails)
admin.site.register(OrderItems)
admin.site.register(ShippingAddress)
