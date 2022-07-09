from django.contrib import auth, messages
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import FormView

from accounts.forms import RegisterForm
from accounts.mixins import AnonymousUserRequiredMixin


class RegisterFormView(AnonymousUserRequiredMixin, FormView):
    """View to handle user registration form submission.

    Page only visible to non-authenticated users.
    Display register template with embedded form on the GET request.
    On form POST, check data validity against model.
    If form data is valid:
    - Create new model instance
    - Log the user in
    - Redirect to homepage
    """

    template_name = "register.html"
    form_class = RegisterForm
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        """Save user model instance, log the user in and trigger toast message."""
        user = form.save()
        auth.login(self.request, user)
        messages.success(
            self.request, f"Account created, welcome {user.username}!")
        return super().form_valid(form)


class LoginFormView(AnonymousUserRequiredMixin, FormView):
    """View to handle user login form submission.

    Page only visible to non-authenticated users.
    Display login template with embedded form on the GET request.
    On form POST, check data validity against model.
    If form data is valid:
    - Check user credentials against credentials stored in database
    - Log the user in
    - Redirect to homepage
    """
    template_name = "login.html"
    form_class = AuthenticationForm

    def get_success_url(self):
        success_url = self.request.GET.get("next")
        if success_url is not None:
            return success_url
        success_url = "home"
        return reverse(success_url)

    def form_valid(self, form):
        """Log the user in and trigger toast message."""
        user = authenticate(
            username=form.cleaned_data["username"],
            password=form.cleaned_data["password"]
        )
        auth.login(self.request, user)
        messages.success(self.request, f"Welcome back {user.username}!")
        return super().form_valid(form)


def logout(request):
    """View to log the user out.

    Remove the user session cookie on request.
    Redirect to the homepage.
    """
    auth.logout(request)
    messages.success(
        request, "See you soon!")
    return redirect("home")
