from django.db import models


class Address(models.Model):
    street = models.CharField(max_length=200)
    lat = models.CharField(max_length=200)
    long = models.CharField(max_length=200)
