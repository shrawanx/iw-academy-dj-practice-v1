from django.db import models


class UserInfo(models.Model):
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()

    dob = models.DateField()
    bio = models.TextField()

    def __str__(self):
        return self.email
