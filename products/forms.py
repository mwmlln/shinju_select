from django import forms
from .models import Product, Category, Tag, ProductImages


class ProductCreateForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Product
        fields = '__all__'


ImageFormset = forms.inlineformset_factory(
                                        Product, ProductImages, fields='__all__',
                                        extra=1,
                                        )

