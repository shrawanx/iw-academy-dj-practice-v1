from django.db import models

COUNTRY_CHOICES = (
    ('NEPAL', 'NEPAL'),
)


class UserInfo(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    is_active = models.BooleanField(default=False)

    country = models.CharField(max_length=100, choices=COUNTRY_CHOICES)
    bio = models.CharField(max_length=200, null=True)

    def save(self, **kwargs):
        self.full_clean()
        return super().save(**kwargs)
