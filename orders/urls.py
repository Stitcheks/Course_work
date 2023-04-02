from django.urls import path, re_path
from .views import get_feedback, order_create

app_name = 'orders'

urlpatterns = [
    path('feedback/', get_feedback, name='feedback'),
    re_path(r'^create/$', order_create, name='order_create'),
    ]
