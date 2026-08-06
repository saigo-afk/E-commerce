from django.db import models

class Products(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, blank=True, null=True)
    stock = models.BooleanField(default=True)
    image = models.ImageField(upload_to='products/', blank=True, null=True)


        
    def __str__(self):
        return self.name


