from django.contrib import admin
from .models import Enquiry


@admin.register(Enquiry)  
class EnquiryAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'status')

