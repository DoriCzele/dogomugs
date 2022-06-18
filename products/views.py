from django.shortcuts import render
from django.views.generic import list, detail
from .models import Product


class ProductListView(list.ListView):

    model = Product
    paginate_by = 6


class ProductDetailView(detail.DetailView):

    model = Product
