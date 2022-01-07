from django.urls import path
from . import views

app_name = 'review'

urlpatterns = [
    path('', views.Review.as_view(), name='reviews'),
    path('create/<int:product_id>/', views.create_review, name='create_review'),
]