from django.apps import AppConfig


class BasketConfig(AppConfig):
    """App configuration for the Basket app."""
    default_auto_field = "django.db.models.BigAutoField"
    name = "basket"
