from django.views.generic.edit import FormView
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from contact.forms import ContactForm


class ContactFormView(FormView):
    template_name = "contact.html"
    form_class = ContactForm
    success_url = reverse_lazy("contact-success")

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return redirect(self.get_success_url())


class ContactSuccessView(TemplateView):
    template_name = "contact_success.html"
