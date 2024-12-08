from django.shortcuts import render
from django.db.models import Count
from .models import Categories

def catalog(request):
    # Получаем все категории с количеством товаров, связанных с каждой категорией
    categories = Categories.objects.annotate(total_products=Count('products')).order_by('id') # 'products' - это обратная связь

    context = {
        'title': 'Aranoz - Catalog',
        'categories': categories,
    }
    return render(request, 'goods/category.html', context)



def product(request):
    context = {
        'title': 'Aranoz - Product',       
    }
    return render(request, 'goods/product.html', context)