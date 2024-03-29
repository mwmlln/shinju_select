from django import forms
from .models import Product, Tag, ProductImages


class ProductForm(forms.ModelForm):
    """ Form to addproduct"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Product
        fields = '__all__'


class ImageForm(forms.ModelForm):
    """ Form to validate image upload and order field"""

    class Meta:
        model = ProductImages
        exclude = ('product',)


class DeleteProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = []
