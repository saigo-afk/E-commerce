from rest_framework import serializers
from .models import Products, Category, Brand


class productSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = [
            'name',
            'description',
            'price',
            'stock',
            'image',
            'category',
        ]


class categorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'name',
            'slug'
        ]


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = [
            'name',
            'logo',
            'description',
        ]


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = __import__('ecommerce.models', fromlist=['Customer']).Customer
        fields = [
            'id',
            'first_name',
            'last_name',
            'address',
            'phone_number',
        ]


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = __import__('ecommerce.models', fromlist=['Order']).Order
        fields = [
            'id',
            'customer',
            'product',
            'count',
            'total_price',
        ]

