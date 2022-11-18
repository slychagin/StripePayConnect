import stripe
from item.models import Item
from django.http import JsonResponse
from django.conf import settings
from django.shortcuts import render
from django.shortcuts import get_object_or_404

stripe.api_key = settings.STRIPE_SECRET_KEY


def buy_item(request, item_id=None):
    item = get_object_or_404(Item, id=item_id)
    context = {
        'item': item,
        'STRIPE_PUBLIC_KEY': settings.STRIPE_PUBLIC_KEY
    }
    return render(request, 'buy_item.html', context)


def create_checkout_session(request, **kwargs):
    item_id = kwargs['pk']
    item = Item.objects.get(id=item_id)
    session = stripe.checkout.Session.create(
        line_items=[{
            'price_data': {
                'currency': 'usd',
                'unit_amount': item.price,
                'product_data': {
                    'name': item.name,
                    'description': item.description
                },
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url='https://stripe-pay-777.herokuapp.com/success/',
        cancel_url='https://stripe-pay-777.herokuapp.com/cancel/',
    )
    return JsonResponse({
        'id': session.id
    })
