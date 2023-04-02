from decimal import Decimal
from django.conf import settings
from main.models import Packing


class Cart (object):
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, packing, quantity=1, update_quantity=False):
        packing_id = str(packing.id)
        if packing_id not in self.cart:
            self.cart[packing_id] = {
                'quantity': 0,
                'price': str(packing.price)
            }
        if update_quantity:
            self.cart[packing_id]['quantity'] = quantity
        else:
            self.cart[packing_id]['quantity'] += quantity
        self.save()

    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

    def remove(self, packing):
        packing_id = str(packing.id)
        if packing_id in self.cart:
            del self.cart[packing_id]
            self.save()

    def __iter__(self):
        product_ids = self.cart.keys()
        packings = Packing.objects.filter(id__in=product_ids)
        for packing in packings:
            self.cart[str(packing.id)]['packing'] = packing

        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def get_total_quantity(self):
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True
