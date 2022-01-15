from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.contrib import messages
from .models import Review, Product
from .forms import ReviewForm, DeleteReviewForm


class ReviewList(ListView):

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
            return redirect(reverse(
                                    'products:product_detail',
                                    args=[product.id]))
            
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


@login_required
def edit_review(request, review_id):
    """
    Edit exisiting review
    """
    review = get_object_or_404(Review, pk=review_id)
    product = review.product
    if request.user != review.user:
        messages.error(request, (
                                'You have no permission to access this page'
                                ))
        return redirect('home')
    if request.method == 'POST':
        review_form = ReviewForm(request.POST, instance=review)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.user = request.user
            review.product = product
            review.save()
            messages.info(request, 'Your review has been updated')
            return redirect(reverse('review:reviews'))
        else:
            messages.error(request, (
                                    'Failed to edit the review. Please ensure'
                                    'the form is valid.'))

    else:
        review_form = ReviewForm(instance=review)

    messages.info(request, 'You are updating your review')
    context = {
        'review_form': review_form,
        'review': review,
        'product': product,
    }
    return render(request, 'review/edit_review.html', context)


@login_required
def delete_review(request, review_id):
    """ Delete a review from the store """

    review = get_object_or_404(Review, pk=review_id)
    if request.user != review.user:
        messages.error(request, (
                                'You have no permission to'
                                'access this page'
                                ))
        return redirect('home')

    form = DeleteReviewForm(request.POST, instance=review)
    if request.method == 'POST':
        if form.is_valid():
            review = form.save(commit=False)
            review.delete()
            messages.success(request, 'The review is successfully deleted')
            return redirect('review:reviews')
    return render(
                request,
                'review/delete_review.html',
                context={'form': form, }
            )
