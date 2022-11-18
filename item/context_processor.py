from item.models import Item


def items_menu(request):
    items = Item.objects.all()
    return dict(items=items)
