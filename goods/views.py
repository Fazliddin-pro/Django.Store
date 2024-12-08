from django.shortcuts import render


def catalog(request):
    context = {
        'title': 'Aranoz - Catalog',
    }
    return render(request, 'goods/category.html', context)


def product(request):
    context = {
        'title': 'Aranoz - Product',       
    }
    return render(request, 'goods/product.html', context)