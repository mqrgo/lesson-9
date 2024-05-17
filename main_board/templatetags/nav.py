from django import template
from main_board.models import Category

register = template.Library()


@register.simple_tag()
def get_nav():
    return Category.objects.all()
