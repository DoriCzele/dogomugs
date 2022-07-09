from django.db import models


class Category(models.Model):
    """Model for product Category"""
    name = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        """String representation for Category."""
        return f"{self.id}: {self.name}"

    class Meta:
        """Meta attributes, defining the plural representation."""
        verbose_name_plural = "Categories"


class Product(models.Model):
    """Model for the Product details."""
    name = models.CharField(max_length=100)
    category = models.ForeignKey(
        Category, blank=True, null=True, on_delete=models.SET_NULL)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=5)
    quantity = models.PositiveIntegerField()
    image = models.ImageField(upload_to="product_images", blank=True)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        """String representation for Product."""
        return self.name

    def sufficient_stock(self, basket_item_quantity):
        """Quantity check for items in basket."""
        if self.quantity < basket_item_quantity or self.active is False:
            return False
        return True

    class Meta:
        """Meta attributes, defining the plural representation."""
        ordering = ("-created",)
