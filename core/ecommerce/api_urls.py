from django.urls import path
from .views import (
    HelloAPIView, ProductAPIView, ProductDetailAPIView,
    BrandAPIView, BrandDetailAPIView,
    CustomerAPIView, CustomerDetailAPIView,
    OrderAPIView, OrderDetailAPIView
)

urlpatterns = [
    path('hello/', HelloAPIView.as_view(), name='hello'),
    
    path('products/', ProductAPIView.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductDetailAPIView.as_view(), name='product-detail'),
    
    path('brands/', BrandAPIView.as_view(), name='brand-list'),
    path('brands/<int:pk>/', BrandDetailAPIView.as_view(), name='brand-detail'),
    
    path('customers/', CustomerAPIView.as_view(), name='customer-list'),
    path('customers/<int:pk>/', CustomerDetailAPIView.as_view(), name='customer-detail'),
    
    path('orders/', OrderAPIView.as_view(), name='order-list'),
    path('orders/<int:pk>/', OrderDetailAPIView.as_view(), name='order-detail'),
]



