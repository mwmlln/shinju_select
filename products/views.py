from django.http import request
from django.shortcuts import render
from django.contrib import messages
from django.views.generic import ListView
from django.db.models import Q
from django.views.generic.detail import DetailView
from .models import Product, Category, Tag
from .forms import ProductForm, ImageForm


class ProductListView(ListView):
    """ A view to show all products, including sorting and search queries """

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


class CategoryListView(ListView):
    """View to display products of specific category"""

    model = Product
    template_name = 'products/products.html'
 
    def get_queryset(self):
        self.category = Category.objects.get(pk=self.kwargs['pk'])
        return Product.objects.filter(category=self.category)


class TagListView(ListView):
    """View to display products of specific tag"""

    model = Product
    template_name = 'products/products.html'
 
    def get_queryset(self):
        self.tag = Tag.objects.get(slug=self.kwargs['pk'])
        return Product.objects.filter(tags=self.tag)


class ProductDetaiView(DetailView):
    """ A view to show individual product details """

    model = Product
    template_name = 'products/product_detail.html'


def add_product(request):
    """ Add a product to the store """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))
     
    if request.method == 'POST':
        product_form = ProductForm(request.POST or None)
        image_form = ImageForm(request.POST, request.FILES)
        if product_form.is_valid() and image_form.is_valid():
            product = product_form.save()
            images = image_form.save(commit=False)
            images = images.save(instance=product)
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(
                        request, 
                        'Failed to add product.'
                        'Please ensure the form is valid.'
                        )

    else:
        product_form = ProductForm()
        image_form = ImageForm()

    template = 'products/add_product.html'
    context = {
        'product_form': product_form,
        'image_form': image_form
    }

    return render(request, template, context)



