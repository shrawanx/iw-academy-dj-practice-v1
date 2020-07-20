from django.db import models


class Info(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.name
