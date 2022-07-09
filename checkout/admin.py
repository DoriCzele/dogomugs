from django.contrib import admin

from checkout.models import OrderDetails, OrderItems, ShippingAddress

admin.site.register(ShippingAddress)
admin.site.register(OrderItems)


class OrderItemsAdmin(admin.TabularInline):
    model = OrderItems


class OrderDetailsAdmin(admin.ModelAdmin):
    inlines = (OrderItemsAdmin,)


admin.site.register(OrderDetails, OrderDetailsAdmin)
