from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from main.models import Packing
from .cart import Cart
from .forms import CartAddProductForm


@require_POST
def cart_add(request, packing_id):
    cart = Cart(request)
    packing = get_object_or_404(Packing, id=packing_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(packing=packing,
                 quantity=cd['quantity'],
                 update_quantity=cd['update']
                 )
    return redirect('cart:cart_detail')


def cart_remove(request, packing_id):
    cart = Cart(request)
    packing = get_object_or_404(Packing, id=packing_id)
    cart.remove(packing)
    return redirect('cart:cart_detail')


def cart_detail(request):
    return render(request, 'cart/detail.html')
