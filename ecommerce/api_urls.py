from django.urls import path
from .views import (ProductListAPIView, HelloAPIView)

urlpatterns = [
    path('hello/', HelloAPIView.as_view(),  name='hello'),
    path('products/', ProductListAPIView.as_view(), name='product-list'),
]

