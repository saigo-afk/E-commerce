from rest_framework import serializers  # type: ignore
from .models import Products, Brand, Customer, Order

class productSerializer(serializers.ModelSerializer):
    class  Meta:
        model = Products
        fields = [
            'name',
            'description',
            'price',
            'image',
            'brand',
            'category',
        ]


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = [
            'id',
            'name',
            'logo',
            'description',
        ]


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = [
            'id',
            'first_name',
            'last_name',
            'address',
            'phone_number',
        ]


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = [
            'id',
            'customer',
            'product',
            'count',
            'total_price',
        ]

