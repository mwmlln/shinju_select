from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from .models import Product


class ProductListView(ListView):
    model = Product
    template_name = 'products/products.html'


class ProductDetaiView(DetailView):
    model = Product
    template_name = 'products/product_detail.html'