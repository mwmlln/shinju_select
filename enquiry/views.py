from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import FormView

from .forms import ContactForm


class ContactFormView(FormView):
    template_name = 'enquiry/contact_form.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact_success')

    def form_valid(self, form):
        pass

    # def form_valid(self, form):
    #     form.send_email()
    #     return super().form_valid(form)


class ContactSuccessView(TemplateView):
    template_name = 'enquiry/contact_success.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['success'] = "Your message is successfully submitted."
        return context