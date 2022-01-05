from django.urls import path
from . import views


urlpatterns = [
    path('', views.Review.as_view(), name='reviews'),
    path('create/<int:product_id>', views.create_review, name='create_review'),
]