from django.forms import ModelForm, Form, CharField, ChoiceField, HiddenInput

from checkout.models import ShippingAddress


class ShippingForm(ModelForm):
    """Form fields for Shipping form."""

    class Meta:
        model = ShippingAddress
        fields = ("full_name", "primary_address", "secondary_address",
                  "town_or_city", "county", "postcode", "country", "phone_number",)


class PaymentForm(Form):
    """Form to retrieve payment information from user.
    Modified from CI course content.
    """
    MONTH_CHOICES = [(i, i) for i in range(1, 12 + 1)]
    YEAR_CHOICES = [(i, i) for i in range(2020, 2036)]

    credit_cc_number = CharField(
        label="Credit card number",
        required=False
    )
    cvv = CharField(
        label="Security code (CVV)",
        required=False
    )
    expiry_month = ChoiceField(
        label="Expiration Month", choices=MONTH_CHOICES, required=False
    )
    expiry_year = ChoiceField(
        label="Expiration Year", choices=YEAR_CHOICES, required=False
    )
    stripe_id = CharField(widget=HiddenInput())
