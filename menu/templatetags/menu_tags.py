from django import template
from django.core.exceptions import ObjectDoesNotExist

from ..models import *

register = template.Library()


@register.inclusion_tag('menu/list_menu.html', takes_context=True)
def draw_menu(context, menu_name):
    current_url = context['request'].path
    item_slug = current_url.split('/')[-2]

    items = Item.objects.filter(menu=menu_name)

    try:
        select_item = items.get(slug=item_slug)
    except ObjectDoesNotExist:
        item = items.get(name=menu_name, parent=None)
        return {'menu': {item: []}}

    children = items.filter(parent=select_item.id)

    menu = {select_item: [{child: []} for child in children]}

    while select_item.parent is not None:
        last_select_item = select_item
        select_item = items.get(id=select_item.parent.id)
        children = items.filter(parent=select_item.id)

        new_level = [{child: []} for child in children if child.id != last_select_item.id]
        new_level.append(menu)

        menu = {select_item: new_level}

    return {'menu': menu, 'select_slug': item_slug}
