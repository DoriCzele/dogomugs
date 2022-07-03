from django.shortcuts import redirect, reverse
from django.views.generic import list, detail
from products.models import Product


class ProductListView(list.ListView):
    """Render a list of Product objects.

    Provide functionality for pagination and searching of Products in a list view.
    """

    model = Product
    paginate_by = 6

    def get(self, request, *args, **kwargs):
        """Override get method to ensure search param is not empty."""
        search_string = self.request.GET.get("search", None)
        if search_string == "":
            # Remove search param when empty search submitted
            return redirect(reverse("product-list"))

        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        """Override get_queryset to enable search Product filtering."""
        queryset = super().get_queryset()
        queryset = queryset.filter(quantity__gt=0)
        search_string = self.request.GET.get("search", None)
        category_filter = self.request.GET.get("category", None)
        if search_string:
            queryset = queryset.filter(
                name__icontains=search_string)
            return queryset
        if category_filter:
            queryset = queryset.filter(category=category_filter)
        return queryset


class ProductDetailView(detail.DetailView):
    """Render a detail view of the Product model instance."""

    model = Product
