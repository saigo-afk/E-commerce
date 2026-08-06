from django.urls import path
from . import views
app_name = "ecommerce"


urlpatterns = [
    path('', views.home, name='home'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('contact/', views.contact, name='contact'),
    path('collection/', views.collection, name='collection'),
]
