from django.shortcuts import redirect, reverse
from django.views.generic import list, detail
from .models import Product


class ProductListView(list.ListView):

    model = Product
    paginate_by = 6

    def get(self, request, *args, **kwargs):
        search_string = self.request.GET.get("search", None)
        if search_string == "":
            # Remove search param when empty search submitted
            return redirect(reverse("product-list"))

        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(quantity__gt=0)
        search_string = self.request.GET.get("search", None)
        if search_string:
            queryset = queryset.filter(
                name__icontains=search_string)
        return queryset


class ProductDetailView(detail.DetailView):

    model = Product
