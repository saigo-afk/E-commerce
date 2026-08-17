from django.contrib import admin
from .models import Products, Order, Brand,Customer,category

admin.site.register(Products)
admin.site.register(category)
admin.site.register(Brand)
admin.site.register(Customer)
admin.site.register(Order)
