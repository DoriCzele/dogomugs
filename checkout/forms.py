from django.forms import ModelForm

from checkout.models import ShippingAddress


class ShippingForm(ModelForm):
    """Form fields for Shipping form."""

    class Meta:
        model = ShippingAddress
        fields = ("full_name", "primary_address", "secondary_address",
                  "town_or_city", "county", "postcode", "country", "phone_number",)
