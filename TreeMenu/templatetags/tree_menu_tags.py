from django import template
from TreeMenu.models import MenuItem
register = template.Library()


@register.inclusion_tag('tags/TreeMenu.html', takes_context=True)
def draw_menu(context, name):
    menu_items = MenuItem.objects.filter(name=name)
    return {
        "menu_items": menu_items,
        "context": context,
        "menu_name": name
    }