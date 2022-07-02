from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=5)
    quantity = models.PositiveIntegerField()
    image = models.ImageField(upload_to="product_images", blank=True)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def sufficient_stock(self, basket_item_quantity):
        if self.quantity < basket_item_quantity or self.active is False:
            return False
        return True

    class Meta:
        ordering = ("-created",)
