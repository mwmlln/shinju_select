from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.db.models import Avg
from django.contrib import messages
from .models import Review, Product
from .forms import ReviewForm


class Review(ListView):

    model = Review
    template_name = 'review/reviews.html'
    paginate_by = 6


@login_required
def create_review(request, product_id):
    """ Diplays Create a review page """
    
    if request.method == 'POST':
        review_form = ReviewForm(request.POST)
        product = get_object_or_404(Product, pk=product_id)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.user = request.user
            review.product = product
            review.save()
            return redirect(reverse('products:product_detail', args=[product.id]))
            
        else:
            messages.error(request,
                           ('Failed to create a review. Please ensure'
                            'the form is valid.'))
    else:
        review_form = ReviewForm()
        product = get_object_or_404(Product, pk=product_id)

    context = {
        'review_form': review_form,
        'product': product
        }
    return render(request, 'review/create_review.html', context)

