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
                            
    def save(self):
        data = self.cleaned_data
        enquiry = Enquiry(
                    name=data['name'],
                    subject=data['subject'],
                    email=data['email'],
                    message=data['message']
                    )
        enquiry.save()
    
    def send_email(self):
        subject = self.cleaned_data['subject']
        message = self.cleaned_data['message']
        name = self.cleaned_data['name']
        email = self.cleaned_data['email']
        recipient_list = [settings.EMAIL_HOST_USER]
        try:
            send_mail(subject, message, email, recipient_list)
        except BadHeaderError:
            return HttpResponse("Invalid header, submission failed")


