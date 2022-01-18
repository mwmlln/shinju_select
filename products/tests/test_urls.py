from django.test import SimpleTestCase
from django.urls import reverse, resolve
from products.views import (
                    ProductListView, CategoryListView, TagListView,
                    ProductDetaiView, add_product, edit_product,
                    delete_product,
                    )


class TestUrls(SimpleTestCase):
    """
    Testing for resolving urls
    """

    def test_products(self):
        """Testing redirect to product list page"""
        url = reverse('products:products')
        self.assertEqual(resolve(url).func.view_class, ProductListView)

    def test_product_product_detail(self):
        """Testing redirect to product detail page"""
        url = reverse('products:product_detail', args=[1])
        self.assertEqual(resolve(url).func.view_class, ProductDetaiView)

    def test_category_list(self):
        """Testing redirect to category list page"""
        url = reverse('products:category_list', args=[1])
        self.assertEqual(resolve(url).func.view_class, CategoryListView)

    def test_tag_list(self):
        """Testing redirect to tag list page"""
        url = reverse('products:tag_list', args=[1])
        self.assertEqual(resolve(url).func.view_class, TagListView)

    def test_add_product(self):
        """Testing redirect to add product page"""
        url = reverse('products:add_product')
        self.assertEqual(resolve(url).func, add_product)

    def test_edit_product(self):
        """Testing redirect to edit product page"""
        url = reverse('products:edit_product', args=[1])
        self.assertEqual(resolve(url).func, edit_product)

    def test_delete_product(self):
        """Testing redirect to delete product page"""
        url = reverse('products:delete_product', args=[1])
        self.assertEqual(resolve(url).func, delete_product)
