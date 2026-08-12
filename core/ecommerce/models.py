from django.db import models

class category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True,null=True,blank=True)

    def __str__(self):
            return self.name


Category = category


class Products(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, blank=True, null=True)
    stock = models.BooleanField(default=True)
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    category = models.ForeignKey(category,on_delete=models.SET_NULL,null=True,blank=True)

    def __str__(self):
            return self.name
    

class Brand(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='brands/', blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
            return self.name
    

class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.TextField()
    phone_number = models.CharField(max_length=15)

    def __str__(self):
            return self.name
    

class Order(models.Model):
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE)
    product = models.ManyToManyField(Products)
    count = models.IntegerField(default=1,blank=True, null=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, blank=True, null=True)


    def __str__(self):
        return self.name


