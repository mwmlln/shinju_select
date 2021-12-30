from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('', views.ProductListView.as_view(), name='products'),
    path('<int:pk>/', views.ProductDetaiView.as_view(), name='product_detail'),
    path(
        'categories/<int:pk>/',
        views.CategoryListView.as_view(),
        name='category_list'
        ),
    path('tags/<str:pk>/', views.TagListView.as_view(), name='tag_list'),
    path('add/', views.add_product, name='add_product'),
]