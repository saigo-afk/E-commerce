from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import render, redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import productSerializer, categorySerializer, BrandSerializer, CustomerSerializer, OrderSerializer
from .forms import contactForm
from .models import Products, Category, Brand, Customer, Order


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
    def get(self, request):
        return Response({"message": "hello, saiman"}, status=status.HTTP_200_OK)


class ProductListAPIView(APIView):
    def get_object(self, pk):
        try:
            return Products.objects.get(pk=pk)
        except Products.DoesNotExist:
            return None

    def get(self, request, pk=None):
        if pk is not None:
            product = self.get_object(pk)
            if product is None:
                return Response({"detail": "Product not found."}, status=status.HTTP_404_NOT_FOUND)
            serializer = productSerializer(product)
            return Response(serializer.data, status=status.HTTP_200_OK)

        products = Products.objects.all()
        serializer = productSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = productSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        if pk is None:
            return Response({"detail": "Product id is required."}, status=status.HTTP_400_BAD_REQUEST)

        product = self.get_object(pk)
        if product is None:
            return Response({"detail": "Product not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = productSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUESTp)

    def delete(self, request, pk=None):
        if pk is None:
            return Response({"detail": "Product id is required."}, status=status.HTTP_400_BAD_REQUEST)

        product = self.get_object(pk)
        if product is None:
            return Response({"detail": "Product not found."}, status=status.HTTP_404_NOT_FOUND)

        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class categoryDetailAPIView(APIView):
    def get_object(self, pk):
        try:
            return Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            return None

    def get(self, request, pk=None):
        if pk is not None:
            category = self.get_object(pk)
            if category is None:
                return Response({"detail": "Category not found."}, status=status.HTTP_404_NOT_FOUND)
            serializer = categorySerializer(category)
            return Response(serializer.data, status=status.HTTP_200_OK)

        categories = Category.objects.all()
        serializer = categorySerializer(categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = categorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        if pk is None:
            return Response({"detail": "Category id is required."}, status=status.HTTP_400_BAD_REQUEST)

        category = self.get_object(pk)
        if category is None:
            return Response({"detail": "Category not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = categorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        if pk is None:
            return Response({"detail": "Category id is required."}, status=status.HTTP_400_BAD_REQUEST)

        category = self.get_object(pk)
        if category is None:
            return Response({"detail": "Category not found."}, status=status.HTTP_404_NOT_FOUND)

        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class brandDetailAPIView(APIView):
    def get(self, request):
        brands = Brand.objects.all()
        serializer = BrandSerializer(brands, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = BrandSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class customerDetailAPIView(APIView):
    def get_object(self, pk):
        try:
            return Customer.objects.get(pk=pk)
        except Customer.DoesNotExist:
            return None

    def get(self, request, pk=None):
        if pk is not None:
            customer = self.get_object(pk)
            if customer is None:
                return Response({"detail": "Customer not found."}, status=status.HTTP_404_NOT_FOUND)
            serializer = CustomerSerializer(customer)
            return Response(serializer.data, status=status.HTTP_200_OK)

        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        if pk is None:
            return Response({"detail": "Customer id is required."}, status=status.HTTP_400_BAD_REQUEST)

        customer = self.get_object(pk)
        if customer is None:
            return Response({"detail": "Customer not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = CustomerSerializer(customer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        if pk is None:
            return Response({"detail": "Customer id is required."}, status=status.HTTP_400_BAD_REQUEST)

        customer = self.get_object(pk)
        if customer is None:
            return Response({"detail": "Customer not found."}, status=status.HTTP_404_NOT_FOUND)

        customer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class orderDetailAPIView(APIView):
    def get_object(self, pk):
        try:
            return Order.objects.get(pk=pk)
        except Order.DoesNotExist:
            return None

    def get(self, request, pk=None):
        if pk is not None:
            order = self.get_object(pk)
            if order is None:
                return Response({"detail": "Order not found."}, status=status.HTTP_404_NOT_FOUND)
            serializer = OrderSerializer(order)
            return Response(serializer.data, status=status.HTTP_200_OK)

        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        if pk is None:
            return Response({"detail": "Order id is required."}, status=status.HTTP_400_BAD_REQUEST)

        order = self.get_object(pk)
        if order is None:
            return Response({"detail": "Order not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = OrderSerializer(order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        if pk is None:
            return Response({"detail": "Order id is required."}, status=status.HTTP_400_BAD_REQUEST)

        order = self.get_object(pk)
        if order is None:
            return Response({"detail": "Order not found."}, status=status.HTTP_404_NOT_FOUND)

        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)