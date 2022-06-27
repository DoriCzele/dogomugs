from django.db import models
from django.contrib.auth.models import User
from products.models import Product


class ShippingAddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100, null=False, blank=False)
    primary_address = models.CharField(max_length=50, null=False, blank=False)
    secondary_address = models.CharField(
        max_length=50, null=False, blank=False)
    town_or_city = models.CharField(max_length=100, null=False, blank=False)
    county = models.CharField(max_length=100, null=False, blank=False)
    postcode = models.CharField(max_length=10, null=False, blank=False)
    country = models.CharField(max_length=50, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.id}: {self.full_name} - {self.primary_address}"

    class Meta:
        verbose_name_plural = "Shipping Addresses"


class OrderDetails(models.Model):
    user = models.OneToOneField(
        User, blank=False, null=True, on_delete=models.SET_NULL)
    shipping_address = models.OneToOneField(
        ShippingAddress, blank=False, null=True, on_delete=models.SET_NULL)
    total_price = models.DecimalField(decimal_places=2, max_digits=8)
    items_quantity = models.IntegerField(null=False, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.id}: {self.user.username}: {self.total_price}"

    class Meta:
        verbose_name_plural = "Orders Details"


class OrderItems(models.Model):
    product = models.OneToOneField(Product, on_delete=models.PROTECT)
    order_details = models.ForeignKey(OrderDetails, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(decimal_places=2, max_digits=5)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.id}: {self.quantity} - {self.product.name}"

    class Meta:
        verbose_name_plural = "Orders Items"
