from django.db import models


class User(models.Model):
    name = models.CharField(max_length=100)


class Address(models.Model):
    street = models.CharField(max_length=100)


class Country(models.Model):
    name = models.CharField(max_length=100)


class UserDetail(models.Model):
    age = models.IntegerField()
    user = models.OneToOneField(User,
                                on_delete=models.CASCADE)

    address = models.ForeignKey(Address,
                                on_delete=models.SET_NULL,
                                null=True,
                                related_name='user_address')

    country = models.ManyToManyField(Country)


class BaseModel(models.Model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        abstract = True


class Information(BaseModel):
    info = models.CharField(max_length=100)
    bio = models.TextField()
