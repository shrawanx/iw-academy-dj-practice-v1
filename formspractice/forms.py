from django import forms
from .models import FormsModel


class MyForm(forms.Form):
    name = forms.CharField(max_length=100)

    email = forms.EmailField()

    my_file = forms.FileField()

    def clean_name(self):
        print("i am from form", self.cleaned_data)
        name = self.cleaned_data['name']
        # i can do any validations or clean the name
        return name.lower()

    # def __str__(self):
    #     return self.as_p()


class FormsModelForm(forms.ModelForm):
    class Meta:
        model = FormsModel
        fields = ['name', 'email']
