from django.contrib.auth.models import User
from django.contrib.messages import get_messages
from django.test import TestCase
from products.models import Category, Product, Tag


class TestProductViews(TestCase):
    """
    A class for testing product views
    """
    def setUp(self):
        """
        Create test user(regular and super user), category and product
        """
        User.objects.create_user(
            username='test_user', password='test_password')
