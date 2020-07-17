from django.forms import ModelForm

from .models import UserInfo


class UserInfoModelForm(ModelForm):
    class Meta:
        model = UserInfo
        fields = ['first_name', 'middle_name', 'last_name', 'email', 'dob', 'bio']
