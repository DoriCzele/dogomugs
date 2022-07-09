from django.views.generic.edit import FormView
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from contact.forms import ContactForm


class ContactFormView(FormView):
    """Form view for Contact Us page."""
    template_name = "contact.html"
    form_class = ContactForm
    success_url = reverse_lazy("contact-success")

    def get_initial(self):
        """Pre-populate form with user's email address if it exists."""
        initial = super().get_initial()
        try:
            if self.request.user.email is not None:
                initial["email_address"] = self.request.user.email
        except AttributeError:
            # AnonymousUser has no 'email' attribute
            pass
        return initial

    def form_valid(self, form):
        """Put logged in user details into contact model."""
        try:
            form.instance.user = self.request.user
        except ValueError:
            # In the case of AnonymousUser
            pass
        form.save()
        return redirect(self.get_success_url())


class ContactSuccessView(TemplateView):
    """Template view for Contact success."""
    template_name = "contact_success.html"
