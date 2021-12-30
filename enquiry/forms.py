from django import forms
from django.conf import settings
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse
from .models import Enquiry


class ContactForm(forms.Form):
    name = forms.CharField(
                        label='',
                        max_length=50,
                        widget=forms.TextInput(attrs={
                                                    'class': 'form-control',
                                                    'placeholder': "Full Name",
                                                    }),
                        )
    subject = forms.CharField(
                        label='',
                        max_length=50,
                        widget=forms.TextInput(attrs={
                                                    'class': 'form-control',
                                                    'placeholder': "Subject",
                                                    }),
                        )
    email = forms.EmailField(
                        label='',
                        widget=forms.EmailInput(attrs={
                                                'class': 'form-control',
                                                'placeholder': "Email address",
                                                }),
                        )
    message = forms.CharField(
                            label='',
                            widget=forms.Textarea(attrs={
                                                'class': 'form-control',
                                                'placeholder': "Message",
                                                }),
                            )
                            
    def send_email(self):
        send_email()


