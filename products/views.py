from django.shortcuts import render
from django.views.generic import list, detail
from .models import Product


class ProductListView(list.ListView):

    model = Product
    paginate_by = 6

    def get_queryset(self):
        search_string = self.request.GET.get("search", None)
        if search_string:
            product_list_queryset = Product.objects.filter(
                name__icontains=search_string)
            return product_list_queryset
        return super().get_queryset()


class ProductDetailView(detail.DetailView):

    model = Product
