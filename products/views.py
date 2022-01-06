from django.http import request
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.db.models import Q
from django.views.generic.detail import DetailView
from .models import Product, Category, Tag
from .forms import ProductForm, ImageForm, DeleteProductForm


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

@login_required
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
            images.product = product
            images.save()
            messages.success(request, 'Successfully added product!')
            return redirect(
                        reverse('products:product_detail', 
                        args=[product.id])
                        )
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


@login_required
def edit_product(request, product_id):
    """ Edit a product in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        product_form = ProductForm(request.POST, instance=product)
        image_form = ImageForm(request.POST, request.FILES, instance=product)
        if product_form.is_valid():
            product_form.save()
            image_form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse(
                                'products:product_detail',
                                args=[product.id])
                                )
        else:
            messages.error(request,
                        ('Failed to update product.'
                         'Please ensure the form is valid.')
                        )
    else:
        product_form = ProductForm(instance=product)
        image_form = ImageForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'product_form': product_form,
        'image_form': image_form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """ Delete a product from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    form = DeleteProductForm(request.POST or None)
    if form.is_valid():
        product.delete()
        messages.success(request, 'The product is successfully deleted')
        return redirect('products:products')
    return render(
                request,
                'products/delete_product.html',
                context={'form': form, }
            )

    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products:products'))