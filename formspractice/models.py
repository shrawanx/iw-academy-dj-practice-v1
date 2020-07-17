from django.db import models


class FormsModel(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
