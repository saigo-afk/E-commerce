from django.test import TestCase
from django.urls import reverse


class ShopPageTests(TestCase):
    def test_home_page_renders(self):
        response = self.client.get(reverse('ecommerce:home'))
        self.assertEqual(response.status_code, 200)

    def test_login_page_renders(self):
        response = self.client.get(reverse('ecommerce:login'))
        self.assertEqual(response.status_code, 200)
