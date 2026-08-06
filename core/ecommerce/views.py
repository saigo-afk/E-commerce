from django.shortcuts import render

from django.http import HttpResponse
from .models import Products


def home(request):
    details = {
        "customer_name": "Yaman Lamichhane",
        "products_count": 12,
    }
    return render(request, "index.html", details)

def aboutus(request):
    return render(request, "aboutus.html")

def contact(request):
    return render(request, "contact.html")


def collection(request):
    products_list = Products.objects.all()
    return render(request, "collection.html", {"products": products_list})


