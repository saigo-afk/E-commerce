from django.shortcuts import render

from django.http import HttpResponse

from django.shortcuts import render

def home(request):
    details = {
        "customer_name": "Yaman Lamichhane",
        "product_count": 12,
    }
    return render(request, "index.html", details)

def aboutus(request):
    return render(request, "aboutus.html")

def contact(request):
    return render(request, "contact.html")


def collection(request):
    products = [
        {
            "name": "gold ring",
            "brand": "El Dorado",
            "price": 100000,
            "description": "This ring is hand made by the artician of city of gold known as El Dorado.",
            "stock": True,
        },
        {
            "name": "sliver necklace",
            "brand": "Italian Jewellers",
            "price": 150000,
            "description": "This necklace is handcrafted by the famous jewlery maker of Italy",
            "stock": True,
        },
        {
            "name": "diamond bracelet",
            "brand": "Duke Malfoy Collection",
            "price": 25000000,
            "description": "This bracelet is set with the finest diamonds and has been wore by wife of the Nobel of England known as Duke Malfoy.",
            "stock": True,
        },
        {
            "name": "platinum earing",
            "brand": "Platinum Jewellers",
            "price": 62000,
            "description": "This earring is made of the finest platinum and is a symbol of elegance.",
            "stock": False,
        }
    ]

    return render(request, "collection.html", {"products": products})


