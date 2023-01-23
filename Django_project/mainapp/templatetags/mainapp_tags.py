from django import template
from mainapp.models import *

register = template.Library()

@register.simple_tag(name='get_category')
def get_categories(filter=None):
    if not filter:
        return Category.objects.all()
    else:
        return Category.objects.filter(pk=filter)

@register.inclusion_tag('list_categories.html')
def show_categories(sort=None, cat_selected=0):
    if not sort:
        category = Category.objects.all()
    else:
        category = Category.objects.order_by(sort)
    return {"category": category, "cat_selected": cat_selected}


