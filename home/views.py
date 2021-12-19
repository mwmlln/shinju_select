from django.shortcuts import render
from django.views.generic import ListView
from products.models import Category

# def index(request):
#     """ A view to return the index page """

#     return render(request, 'home/index.html')

class HomeView(ListView):
    model = Category
    template_name = 'home/index.html'