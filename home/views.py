from django.shortcuts import render
from django.views.generic import ListView
from products.models import Category


class HomeView(ListView):
    model = Category
    template_name = 'home/index.html'