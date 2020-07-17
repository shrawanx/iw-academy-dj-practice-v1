from django.db import models

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    middle_name = models.CharField(max_length=100)

    groups = None
    user_permissions = None

    @staticmethod
    def get_bio():
        return "Hi this is My Bio"

# class UserDetail(models.Model):
#     phone_number = models.CharField(max_length=100)
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
