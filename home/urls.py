from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('delivery/', views.DeliveryView.as_view(), name='delivery'),
    path('faqs/', views.FaqsView.as_view(), name='faqs')
]
