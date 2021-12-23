from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.base import TemplateView
from products.models import Category


class HomeView(ListView):
    model = Category
    template_name = 'home/index.html'


class AboutView(TemplateView):
    template_name = 'home/about.html'


class DeliveryView(TemplateView):
    template_name = 'home/delivery.html'
