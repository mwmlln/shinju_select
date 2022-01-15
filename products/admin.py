from django.contrib import admin
from .models import (
    Tag, Category, Product, ProductImages
)


class TagInline(admin.TabularInline):
    model = Product.tags.through


class ImageInLine(admin.TabularInline):
    model = ProductImages


class ImageAdmin(admin.ModelAdmin):
    raw_id_field = ['product']


class ProductAdmin(admin.ModelAdmin):
    inlines = [TagInline, ImageInLine]
    exclude = ['tags']

admin.site.register(Product, ProductAdmin)
admin.site.register(
    [Tag, Category]
)
admin.site.register(ProductImages, ImageAdmin)
