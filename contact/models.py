from django.db import models
from django.contrib.auth.models import User


class Contact(models.Model):
    """Model for Contact."""
    user = models.ForeignKey(
        User, blank=True, null=True, on_delete=models.SET_NULL)
    email_address = models.EmailField()
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        """String representation for Contact model."""
        return f"{self.id}: {self.email_address}"

    class Meta:
        verbose_name_plural = "Contact messages"
