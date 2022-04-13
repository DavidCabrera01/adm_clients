from datetime import date
from django.db import models

# Create your models here.


class Client(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()

class Phone(models.Model):
    cliente_id = models.ForeignKey(Client, on_delete=models.CASCADE)
    country_code = models.CharField(max_length=100)
    phone = models.CharField(max_length=50)

class Country(models.Model):
    name = models.CharField(max_length=50)

class Address(models.Model):
    cliente_id = models.ForeignKey(Client, on_delete=models.CASCADE)
    stret = models.CharField(max_length=50)
    number = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=10)
    state = models.CharField(max_length=50)
    country_id = models.ForeignKey(Country, on_delete=models.CASCADE)

class Order(models.Model):
    cliente_id = models.ForeignKey(Client, on_delete=models.CASCADE)
    date = models.DateField()

class Item(models.Model):
    ordern_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    description = models.CharField(max_length=50)
    value = models.PositiveIntegerField()
    amount = models.PositiveIntegerField()


