from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    context = {
        'title': 'Aranoz',
    }
    return render(request, 'main/index.html', context)


def contact(request):
    context = {
        'title': 'Aranoz - Contact Us',
    }
    return render(request, 'main/contact.html', context)