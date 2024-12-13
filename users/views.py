from django.contrib import auth
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse

from users.forms import UserLoginForm, UserRegistrationForm
from users.models import User


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserLoginForm()

    context = {
        'title': 'Aranoz - Login',
        'form': form,
    }
    return render(request, 'users/login.html', context)


def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            user = form.instance
            auth.login(request, user)  # Авторизация после регистрации
            return HttpResponseRedirect(reverse('main:index'))  # Перенаправление на страницу логина
    else:
        form = UserRegistrationForm()
    
    countries = User._meta.get_field('country').choices

    context = {
        'title': 'Aranoz - Registration',
        'countries': countries,
        'form': form,
    }
    return render(request, 'users/registration.html', context)


def checkout(request):
    context = {
        'title': 'Aranoz - Checkout',
    }
    return render(request, 'users/checkout.html', context)


def logout(request):
    auth.logout(request)
    return redirect(reverse('main:index'))
