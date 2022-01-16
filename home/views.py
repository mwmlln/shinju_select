from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.base import TemplateView
from products.models import Category


class HomeView(ListView):
    """View to display landing page"""
    model = Category
    template_name = 'home/index.html'


class AboutView(TemplateView):
    """View to display about page"""
    template_name = 'home/about.html'


class DeliveryView(TemplateView):
    """View to display delivery info page"""
    template_name = 'home/delivery.html'


class FaqsView(TemplateView):
    """View to display delivery info page"""
    template_name = 'home/faqs.html'
