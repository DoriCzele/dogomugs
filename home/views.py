from django.views.generic import TemplateView
from home.models import FrequentlyAskedQuestion


class HomeView(TemplateView):
    template_name = "home.html"

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        questions = FrequentlyAskedQuestion.objects.all()
        context["questions"] = questions
        return super().render_to_response(context)
