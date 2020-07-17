from django.db import models
from django.core.exceptions import ValidationError


def validate_my_age(age):
    if age < 20:
        raise ValidationError("You age should be more or equals to 20")


class UserBio(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    age = models.IntegerField(validators=[validate_my_age])

    bio = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.name

    # # if user age > 40 then bio is compulsory
    def clean(self):
        if self.age > 40:
            if not self.bio:
                raise ValidationError("Bio is required when age > 40")
