from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import render, redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import productSerializer
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


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ecommerce:login')
    else:
        form = UserCreationForm()
    return render(request, 'ecommerce/register.html', {'form': form})


def login_view(request):
    error_message = None
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('ecommerce:home')
        error_message = "Invalid username or password."
    else:
        form = AuthenticationForm()
    return render(request, 'ecommerce/login.html', {'form': form, 'error_message': error_message})


def logout_view(request):
    logout(request)
    return redirect('ecommerce:home')


@login_required
def profile(request):
    return render(request, "ecommerce/profile.html", {"user": request.user})


def cart(request):
    return render(request, "ecommerce/cart.html")



class HelloAPIView(APIView):
    def get(self,request):
        return Response(
            {"message": "hello, saiman"},
            status=status.HTTP_200_Ok
        )


class ProductListAPIView(APIView):
    def get(self,request):
        Products=Products.objects.all()
        serializer=productSerializer(
            Products, many=True)
        return Response(serializer.data, status=status.Http_200_Ok)

def post(self, request):
    serializer = productSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)