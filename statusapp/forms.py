from django.forms import ModelForm
from .models import StatusMessage


class StatusMessageModelForm(ModelForm):
    class Meta:
        model = StatusMessage
        fields = ['status']
