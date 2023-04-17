from django.shortcuts import render
from main.models import Product
from cart.forms import CartAddProductForm
from .models import OrderItem
from .forms import ContactModelForm, OrderCreateForm
from cart.cart import Cart


def get_feedback(request):
    form = ContactModelForm(request.POST)
    if request.method == 'POST':
        form = ContactModelForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'orders/feedback/get_feedback.html', context={'form': form})
        else:
            return render(request, 'utils/error_feedback.html')
    return render(request, 'orders/feedback/feedback.html', context={'form': form})


def get_product(request, pk=None):
    if Product.objects.filter(pk=pk).exists():
        product = Product.objects.get(pk=pk)
        cart_product_form = CartAddProductForm()

        context = {'product': product, 'cart_product_form': cart_product_form}
        return render(request, 'products/detail.html', context)
    else:
        return render(request, 'utils/404.html')


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user_id = request.user
            order.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         packing=item['packing'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            cart.clear()
            return render(request, 'orders/order/created.html', context={'order': order})
        else:
            print(form.errors)
    else:
        form = OrderCreateForm
    return render(request, 'orders/order/create.html', context={'form': form})
