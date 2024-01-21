from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=False)
    name = models.CharField(max_length=255, null=True, blank=False)
    email = models.CharField(max_length=255, null=True, blank=False)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255, null=True, blank=False)
    price = models.FloatField(default=0.00, null=True, blank=False)
    digital = models.BooleanField(default=False, null=True, blank=False)

    def __str__(self):
        return self.name

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=False, null=True)
    date_order = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=False)
    transaction_id = models.CharField(max_length=255, null=True)

    def __str__(self):
        return str(self.id)

class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=False, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=False, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)

class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=False, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=False, null=True)
    address = models.CharField(max_length=255, null=True, blank=False)
    city = models.CharField(max_length=255, null=True, blank=False)
    phone = models.CharField(max_length=255, null=True, blank=False)
    state = models.CharField(max_length=255, null=True, blank=False)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.address)

