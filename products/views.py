from django.http import request
from django.shortcuts import render
from django.contrib import messages
from django.views.generic import ListView
from django.db.models import Q
from django.views.generic.detail import DetailView
from .models import Product, Category, Tag
# from .forms import ProductForm, ImageForm
from .forms import ProductCreateForm, ImageFormset


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


class CategoryListView(ListView):
    model = Product
    template_name = 'products/products.html'
 
    def get_queryset(self):
        self.category = Category.objects.get(pk=self.kwargs['pk'])
        return Product.objects.filter(category=self.category)


class TagListView(ListView):
    model = Product
    template_name = 'products/products.html'
 
    def get_queryset(self):
        self.tag = Tag.objects.get(slug=self.kwargs['pk'])
        return Product.objects.filter(tags=self.tag)


class ProductDetaiView(DetailView):
    model = Product
    template_name = 'products/product_detail.html'


def add_product(request):
    form = ProductCreateForm(request.POST or None)
    context = {'form': form}
    if request.method == 'POST' and form.is_valid():
        product = form.save(commit=False)
        # image_formset = ImageFormset(request.POST, files=request.FILES, instance=product)  # 増えた
        if file_formset.is_valid(): # and image_formset.is_valid():   # image_formset.is_valid()が増えた
            product.save()
            file_formset.save()
            # image_formset.save()  
            return redirect('products:products')

        else:
            # context['image_formset'] = image_formset
            pass 

    else:
        # context['image_formset'] = ImageFormset()  
        pass

    return render(request, 'products/add_product.html', context)
