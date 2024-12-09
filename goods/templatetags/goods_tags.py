from django import template
from django.db.models import Count

from goods.models import Categories


register = template.Library()

@register.simple_tag()
def tag_categories():
    return Categories.objects.annotate(total_products=Count("products")).order_by("id") #'products' - это обратная связь

