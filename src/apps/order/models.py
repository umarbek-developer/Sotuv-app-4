from django.db import models
from apps.product.models import Product 
from apps.customer.models import Customer
from apps.users.models import Stuff

# Create your models here.

class Cart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    staff = models.ForeignKey(Stuff, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"{self.product}"


class Order(models.Model):
    customer = models.ForeignKey(Product, on_delete=models.CASCADE)
    staff = models.ForeignKey(Customer, on_delete=models.CASCADE)
    total_price = models.DecimalField(default=0, decimal_places=4, max_digits=4)
    PAYMENT_CHOICES = [
        ("Cash", "Cash"),
        ("Cart", "Cart")
    ]
    payment_type = models.CharField(max_length=10, choices=PAYMENT_CHOICES)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.customer}"
    

class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    staff = models.ForeignKey(Stuff, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    total_price = models.DecimalField(default=0, decimal_places=4, max_digits=4)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"{self.product}"


