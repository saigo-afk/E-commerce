from django.urls import path
from .views import (ProductListAPIView, HelloAPIView, categoryDetailAPIView, brandDetailAPIView, customerDetailAPIView, orderDetailAPIView)

urlpatterns = [
    path('hello/', HelloAPIView.as_view(), name='hello'),
    path('products/', ProductListAPIView.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductListAPIView.as_view(), name='product-detail'),
    path('category/', categoryDetailAPIView.as_view(), name='category-details'),
    path('category/<int:pk>/', categoryDetailAPIView.as_view(), name='category-detail'),
    path('brands/', brandDetailAPIView.as_view(), name='brand-details'),
    path('customers/', customerDetailAPIView.as_view(), name='customer-details'),
    path('customers/<int:pk>/', customerDetailAPIView.as_view(), name='customer-detail'),
    path('orders/', orderDetailAPIView.as_view(), name='order-details'),
    path('orders/<int:pk>/', orderDetailAPIView.as_view(), name='order-detail'),
]

