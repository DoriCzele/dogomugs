from django import forms
from django.forms import ValidationError
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class RegisterForm(UserCreationForm):
    """Form fields for Registration form."""
    email = forms.EmailField()

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise ValidationError(
                "An account with this email address already exists.")
        return email

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
