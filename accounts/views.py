from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model

from .forms import LoginForm, SignUpForm

USER = get_user_model()


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            user = authenticate(username=form.cleaned_data['username'],
                                password=form.cleaned_data['password'])
            if user:
                print(" a user is found", user)
                login(request, user)
                return redirect('/accounts/profile/')
            else:
                print("auth credentials do not match")
    elif request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('/accounts/profile/')
        form = LoginForm()

    return render(request,
                  'accounts/login.html',
                  {'form': form})


@login_required()
def profile_view(request):
    # this context is passed for statusapp
    from statusapp.models import StatusMessage
    # messages = StatusMessage.objects.filter(user=request.user)
    messages = StatusMessage.objects.filter(user_id=request.user.id)
    # messages = StatusMessage.objects.all()
    return render(request, 'accounts/profile.html', {
        'messages': messages
    })


def logout_view(request):
    logout(request)
    return redirect('/accounts/login/')


def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            print("form is valid")
            print(form.cleaned_data)
            user = USER(
                username=form.cleaned_data['username'],
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
            )
            user.save()
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('/accounts/login/')

    elif request.method == 'GET':
        form = SignUpForm()

    return render(request, 'accounts/signup.html', {'form': form})
