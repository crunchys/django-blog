from django import template
from app.models import *


register = template.Library()


@register.inclusion_tag('app/list_categories.html')
def show_categories(sort=None, category_selected=0):
    if not sort:
        categories = Category.objects.all()
    else:
        categories = Category.objects.order_by(sort)
    return {'categories': categories, 'category_selected': category_selected}
