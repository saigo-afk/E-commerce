from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User


class ShopPageTests(TestCase):
    def test_home_page_renders(self):
        response = self.client.get(reverse('ecommerce:home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'WELCOME TO SAIJEWL')

    def test_login_page_renders(self):
        response = self.client.get(reverse('ecommerce:login'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Welcome Back')

    def test_profile_page_requires_login(self):
        response = self.client.get(reverse('ecommerce:profile'))
        self.assertEqual(response.status_code, 302)

    def test_authenticated_profile_page_renders(self):
        user = User.objects.create_user(username='demo', password='demo1234')
        self.client.force_login(user)
        response = self.client.get(reverse('ecommerce:profile'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Your Profile')

    def test_cart_and_wishlist_pages_render(self):
        for name in ['cart', 'wishlist']:
            response = self.client.get(reverse(f'ecommerce:{name}'))
            self.assertEqual(response.status_code, 200)
