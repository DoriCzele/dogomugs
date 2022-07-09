from django.views.generic import TemplateView
from home.models import FrequentlyAskedQuestion


class HomeView(TemplateView):
    """View for the homepage."""
    template_name = "home.html"

    def get(self, request, *args, **kwargs):
        """Fetch all FrequentlyAskedQuestions and put into context."""
        context = self.get_context_data(**kwargs)
        questions = []
        try:
            questions = FrequentlyAskedQuestion.objects.all()
        except FrequentlyAskedQuestion.DoesNotExist:
            pass

        context["questions"] = questions
        return super().render_to_response(context)
