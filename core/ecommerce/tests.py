from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Products, Category


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

    def test_cart_page_renders(self):
        response = self.client.get(reverse('ecommerce:cart'))
        self.assertEqual(response.status_code, 200)


class ApiTests(TestCase):
    def test_hello_api_returns_message(self):
        response = self.client.get('/api/hello/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['message'], 'hello, saiman')

    def test_products_api_returns_all_products(self):
        category = Category.objects.create(name='Shoes', slug='shoes')
        Products.objects.create(
            name='Running Shoes',
            description='Comfortable pair',
            price='99.99',
            stock=True,
            category=category,
        )

        response = self.client.get('/api/products/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 1)
        self.assertEqual(response.json()[0]['name'], 'Running Shoes')

    def test_product_put_and_delete_api_work(self):
        category = Category.objects.create(name='Shoes', slug='shoes')
        product = Products.objects.create(
            name='Old Shoes',
            description='Old description',
            price='49.99',
            stock=True,
            category=category,
        )

        put_response = self.client.put(
            f'/api/products/{product.pk}/',
            {
                'name': 'Updated Shoes',
                'description': 'New description',
                'price': '79.99',
                'stock': True,
                'category': category.pk,
            },
            content_type='application/json',
        )
        self.assertEqual(put_response.status_code, 200)
        product.refresh_from_db()
        self.assertEqual(product.name, 'Updated Shoes')

        delete_response = self.client.delete(f'/api/products/{product.pk}/')
        self.assertEqual(delete_response.status_code, 204)
        self.assertFalse(Products.objects.filter(pk=product.pk).exists())

    def test_category_put_and_delete_api_work(self):
        category = Category.objects.create(name='Accessories', slug='accessories')

        put_response = self.client.put(
            f'/api/category/{category.pk}/',
            {
                'name': 'Updated Accessories',
                'slug': 'updated-accessories',
            },
            content_type='application/json',
        )
        self.assertEqual(put_response.status_code, 200)
        category.refresh_from_db()
        self.assertEqual(category.name, 'Updated Accessories')

        delete_response = self.client.delete(f'/api/category/{category.pk}/')
        self.assertEqual(delete_response.status_code, 204)
        self.assertFalse(Category.objects.filter(pk=category.pk).exists())
