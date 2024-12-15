from django.contrib.auth.decorators import login_required
from django.contrib import auth, messages
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse

from users.forms import CheckoutForm, UserLoginForm, UserRegistrationForm
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
                messages.success(request, f'{username}, you have logged in successfully!')
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
            messages.success(request, f'{user.username}, you have registered successfully!')
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

@login_required
def checkout(request):
    if request.method == 'POST':
        form = CheckoutForm(data=request.POST, instance=request.user, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated successfully!')
            return HttpResponseRedirect(reverse('user:checkout'))  # Перенаправление на страницу логина
    else:
        form = CheckoutForm(instance=request.user)
    
    countries = User._meta.get_field('country').choices

    context = {
        'title': 'Aranoz - Checkout',
        'form': form,
        'countries': countries,
    }
    return render(request, 'users/checkout.html', context)

@login_required
def logout(request):
    auth.logout(request)
    messages.success(request, 'You have logged out successfully!')
    return redirect(reverse('main:index'))
