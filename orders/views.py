from django.views.generic import list, detail
from django.contrib.auth.mixins import LoginRequiredMixin
from checkout.models import OrderDetails


class OrderDetailsListView(LoginRequiredMixin, list.ListView):
    """Render a list of OrderDetails objects.

    Provide functionality for pagination and searching of OrderDetails in a list view.
    """

    model = OrderDetails
    paginate_by = 6
    template_name = "order_list.html"

    def get_queryset(self):
        """Override get_queryset to enable search OrderDetails filtering."""
        queryset = super().get_queryset()
        queryset = queryset.filter(
            user=self.request.user, items_quantity__gt=0).order_by("-updated")
        return queryset


class OrderDetailsDetailView(LoginRequiredMixin, detail.DetailView):
    """Render a detail view of the OrderDetails model instance."""

    model = OrderDetails
    template_name = "order_detail.html"

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
