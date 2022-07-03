from django.forms import ModelForm

from contact.models import Contact


class ContactForm(ModelForm):
    """Form fields for Contact form."""

    class Meta:
        model = Contact
        fields = ("email_address", "message")
