from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, render

from .forms import contactForm
from .models import Products


def home(request):
    details = {
        "customer_name": "Yaman Lamichhane",
        "products_count": 12,
    }
    return render(request, "ecommerce/index.html", details)


def aboutus(request):
    return render(request, "ecommerce/aboutus.html")


def contact(request):
    form = contactForm()
    return render(request, "ecommerce/contact.html", {"Form": form})


def collection(request):
    products_list = Products.objects.all()
    return render(request, "ecommerce/collection.html", {"products": products_list})


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("ecommerce:profile")
    else:
        form = AuthenticationForm()

    return render(request, "ecommerce/login.html", {"form": form})


@login_required
def profile(request):
    return render(request, "ecommerce/profile.html", {"user": request.user})


def cart(request):
    return render(request, "ecommerce/cart.html")


def wishlist(request):
    return render(request, "ecommerce/wishlist.html")


