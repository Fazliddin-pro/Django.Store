from django.shortcuts import render

from .models import Categories, Products


def catalog(request):

    goods = Products.objects.all()

    context = {
        "title": "Aranoz - Catalog",
        "goods": goods,
    }
    return render(request, "goods/catalog.html", context)


def product(request):
    context = {
        "title": "Aranoz - Product",
    }
    return render(request, "goods/product.html", context)
