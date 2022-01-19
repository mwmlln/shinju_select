from django.contrib.messages import get_messages
from django.test import TestCase


class TestHometViews(TestCase):

    def test_get_home(self):
        """Testing home page url"""
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/index.html')

    def test_get_about(self):
        """Testing about page url"""
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/about.html')

    def test_get_delivery(self):
        """Testing delivery page url"""
        response = self.client.get('/delivery/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/delivery.html')

    def test_get_delivery(self):
        """Testing faqs page url"""
        response = self.client.get('/faqs/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/faqs.html')
