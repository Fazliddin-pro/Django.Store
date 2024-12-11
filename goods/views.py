from django.core.paginator import Paginator
from django.shortcuts import get_list_or_404, render

from goods.utils import q_search

from .models import Products


def catalog(request, category_slug=None):

    page = request.GET.get('page', 1)
    order_by = request.GET.get('order_by', 'default')
    on_sale = request.GET.get('on_sale', None)
    query = request.GET.get('q', None)

    # Получаем товары в зависимости от категории
    if category_slug == 'all':
        goods = Products.objects.all()
    elif query:
        goods = q_search(query)
    else:
        goods = Products.objects.filter(category__slug=category_slug)

    # Фильтрация по скидке
    if on_sale:  # Проверяем, если чекбокс был установлен
        goods = goods.filter(discount__gt=0)

    # Сортировка по цене
    if order_by != 'default':
        goods = goods.order_by(order_by)

    # Пагинация
    paginator = Paginator(goods, 6)
    current_page = paginator.get_page(page)

    context = {
        "title": "Aranoz - Catalog",
        "goods": current_page,
        "category_slug": category_slug,
    }

    return render(request, "goods/catalog.html", context)


def product(request, product_slug):

    product = Products.objects.get(slug=product_slug)

    context = {
        "title": "Aranoz - Product",
        "product": product
    }
    return render(request, "goods/product.html", context)
