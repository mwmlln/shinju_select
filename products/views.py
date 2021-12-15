from django.http import request
from django.shortcuts import render
from django.contrib import messages
from django.views.generic import ListView
from django.db.models import Q
from django.views.generic.detail import DetailView
from .models import Product


class ProductListView(ListView):
    model = Product
    template_name = 'products/products.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
 
        if query:
            object_list = Product.objects.filter(
                Q(name__icontains=query) | Q(description__icontains=query)
                )
        else:
            object_list = Product.objects.all()
        return object_list


class ProductDetaiView(DetailView):
    model = Product
    template_name = 'products/product_detail.html'