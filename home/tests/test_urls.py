from django.test import SimpleTestCase
from django.urls import reverse, resolve
from home.views import HomeView, AboutView, DeliveryView, FaqsView


class TestUrls(SimpleTestCase):
    """
    Testing for resolving urls
    """

    def test_home(self):
        """Testing redirect to index page"""
        url = reverse('home')
        self.assertEqual(resolve(url).func.view_class, HomeView)

    def test_about(self):
        """Testing redirect to about page"""
        url = reverse('about')
        self.assertEqual(resolve(url).func.view_class, AboutView)

    def test_delivery(self):
        """Testing redirect to delivery page"""
        url = reverse('delivery')
        self.assertEqual(resolve(url).func.view_class, DeliveryView)

    def test_faqs(self):
        """Testing redirect to FAQ page"""
        url = reverse('faqs')
        self.assertEqual(resolve(url).func.view_class, FaqsView)
