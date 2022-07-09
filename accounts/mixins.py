from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib import messages
from django.shortcuts import redirect


class AnonymousUserRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        """Test if user is anonymous, otherwise trigger toast message."""
        if self.request.user.is_anonymous:
            return True
        messages.error(
            self.request, "You are already logged in.")
        return False

    def handle_no_permission(self):
        """Redirect to home if user is not anonymous."""
        return redirect("home")
