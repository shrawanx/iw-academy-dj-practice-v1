from django.shortcuts import render
from django.http import HttpResponse

from .forms import MyForm, FormsModelForm


def forms_home(request):
    if request.method == 'GET':
        return render(request, 'formspractice/forms.html', {})
    else:  # post
        print(request.POST.get('name'))
        return HttpResponse("OKOK")


def django_form(request):
    if request.method == 'GET':
        form = MyForm()
        return render(request, 'formspractice/django_form.html', {'form': form})
    else:  # post
        form = MyForm(request.POST)
        if form.is_valid():
            print("after validation on views", form.cleaned_data)
            return HttpResponse("OK")
        else:
            return render(request, 'formspractice/django_form.html', {'form': form})


def django_model_form(request):
    if request.method == 'GET':
        form = FormsModelForm()
        return render(request, 'formspractice/forms_model.html', {'form': form})
    else:  # post
        form = FormsModelForm(request.POST)
        if form.is_valid():
            form.save()
            print("after validation on views", form.cleaned_data)
            return HttpResponse("OK")
        else:
            return render(request, 'formspractice/forms_model.html', {'form': form})
