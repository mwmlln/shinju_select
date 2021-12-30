from django import forms
from .models import Product, Category, Tag, ProductImages


class ProductForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Product
        fields = '__all__'


class ImageForm(forms.ModelForm):

    class Meta:
        model = ProductImages
        exclude = ('product',)
