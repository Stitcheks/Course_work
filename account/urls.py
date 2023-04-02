from django.urls import re_path
from .views import user_login, register, edit, user_logout

app_name = 'account'

urlpatterns = [
    re_path(r'^login/$', user_login, name='login'),
    re_path(r'^logout/$', user_logout, name='logout'),
    re_path(r'^register/$', register, name='register'),
    re_path(r'^edit/$', edit, name='edit'),
]