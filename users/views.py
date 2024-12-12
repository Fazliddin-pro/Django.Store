from django.shortcuts import render


def login(request):
    context = {
        'title': 'Aranoz - Login',
    }
    return render(request, 'users/login.html', context)


def registration(request):
    context = {
        'title': 'Aranoz - Registration',
    }
    return render(request, 'users/registration.html', context)


def checkout(request):
    context = {
        'title': 'Aranoz - Checkout',
    }
    return render(request, 'users/checkout.html', context)


def logout(request):
    pass
