from django.shortcuts import render
from cart.forms import CartAddProductForm
from cart.cart import Cart
from .models import Catalog, Product, Brand, ProductType
from django.views.generic import ListView


def get_main_page(request):
    cats = Catalog.objects.all()
    brands = Brand.objects.all()
    prods = Product.objects.all()
    context = {'cats': cats, 'prods': prods, 'brands': brands}
    return render(request, 'main/main_page.html', context)


def get_catalog(request):
    cats = Catalog.objects.all()
    prods = Product.objects.all()
    cart_product_form = CartAddProductForm()
    context = {'cats': cats, 'prods': prods, 'cart_product_form': cart_product_form}
    return render(request, 'main/get_catalog.html', context)


class SearchResultsView(ListView):
    model = Product
    template_name = 'main/search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Product.objects.filter(name__icontains=query)
        return object_list


def cat_filter(request, cat_pk=None):
    cats = Catalog.objects.all()
    cart_product_form = CartAddProductForm()
    if Product.objects.filter(catalog_id=cat_pk).exists():
        products = Product.objects.filter(catalog_id=cat_pk)
        context = {'cats': cats, 'products': products, 'cart_product_form': cart_product_form}
        return render(request, 'main/cat_filter.html', context)
    else:
        return render(request, 'utils/404.html')


def cat_ptype_filter(request, cat_pk=None, id=None):
    cats = Catalog.objects.all()
    cart_product_form = CartAddProductForm()
    if Product.objects.filter(catalog=cat_pk).exists():
        products = Product.objects.filter(catalog_id=cat_pk)
    else:
        return render(request, 'utils/404.html')
    if products.filter(product_type_id=id).exists():
        products = products.filter(product_type_id=id)
        product_type = ProductType.objects.filter(id=id)
        context = {'cats': cats,
                   'products': products,
                   'product_type': product_type,
                   'cart_product_form': cart_product_form}
        return render(request, 'main/cat_ptype_filter.html', context)
    else:
        return render(request, 'utils/no_results.html', context={'cats': cats,
                                                                 'products': products,
                                                                 'cart_product_form': cart_product_form}
                      )


def cat_clarification_filter(request, cat_pk=None, id=None, clar_id=None):
    cats = Catalog.objects.all()
    cart_product_form = CartAddProductForm()
    if Product.objects.filter(catalog_id=cat_pk).exists():
        products = Product.objects.filter(catalog_id=cat_pk)
    else:
        return render(request, 'utils/404.html')
    if products.filter(product_type_id=id).exists():
        products = products.filter(product_type_id=id)
        product_type = ProductType.objects.filter(id=id)
    else:
        context = {'cats': cats,
                   'products': products,
                   'cart_product_form': cart_product_form}
        return render(request, 'utils/no_results.html', context)

    if products.filter(clarification_id=clar_id):
        products = products.filter(clarification_id=clar_id)

        context = {
            'cats': cats,
            'products': products,
            'cart_product_form': cart_product_form,
            'product_type': product_type
        }
        return render(request, 'main/cat_clarification_filter.html', context)
    else:
        return render(request, 'utils/no_results.html', context={'cats': cats,
                                                                 'products': products,
                                                                 'cart_product_form': cart_product_form})
