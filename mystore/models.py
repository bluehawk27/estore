from __future__ import unicode_literals

from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=850)
    price = models.FloatField()
    description = models.TextField()
    imglink = models.CharField(max_length=500)


class Order(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.CharField(max_length=500)
    city = models.CharField(max_length=300)
    payment_method = models.CharField(max_length=400)
    payment_data = models.CharField(max_length=400)
    items = models.TextField()
    fulfilled = models.BooleanField()
