from django.urls import path
from . import views

urlpatterns = [
    path('', views.ContactFormView.as_view(), name='enquiry'),
    path(
        'contact_success/',
        views.ContactSuccessView.as_view(),
        name='contact_success'
        ),
]
