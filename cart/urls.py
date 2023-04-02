from django.urls import path, re_path
from . import views

app_name = 'cart'

urlpatterns = [
    re_path(r'^add/(?P<packing_id>\d+)/$', views.cart_add, name='cart_add'),
    re_path(r'^remove/(?P<packing_id>\d+)/$', views.cart_remove, name='cart_remove'),
    path(r'^$', views.cart_detail, name='cart_detail'),
]