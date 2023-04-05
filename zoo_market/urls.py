from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from orders.views import get_product


urlpatterns = [
    path('admin/', admin.site.urls),
    path('orders/', include('orders.urls')),
    path('catalog/', include('orders.urls')),
    path('feedback/', include('orders.urls')),
    re_path(r'^account/', include('account.urls')),
    re_path(r'^orders/', include('orders.urls', namespace='orders')),
    re_path(r'^cart/', include('cart.urls', namespace='cart')),
    re_path(r'^cat_filter/', include('main.urls')),
    path('<int:pk>', get_product, name='product_detail'),
    path('', include('main.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
