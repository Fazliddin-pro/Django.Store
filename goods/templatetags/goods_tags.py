from django import template
from django.db.models import Count
from django.utils.http import urlencode

from goods.models import Categories


register = template.Library()

@register.simple_tag()
def tag_categories():
    return Categories.objects.annotate(total_products=Count("products")).order_by("id") #'products' - это обратная связь


@register.simple_tag(takes_context=True)
def change_params(context, **kwargs):
    query = context['request'].GET.dict()
    query.update(kwargs)
    return urlencode(query)