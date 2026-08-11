from rest_framework import serializers  # type: ignore
from .models import Products

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
