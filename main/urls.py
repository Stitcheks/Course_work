from django.urls import path
from .views import get_main_page, SearchResultsView, get_catalog, cat_filter, cat_ptype_filter, cat_clarification_filter

app_name = 'main'

urlpatterns = [
    path('catalog/', get_catalog, name='catalog'),
    path('cat_filter/<int:cat_pk>', cat_filter, name='cat_filter'),
    path('cat_ptype_filter/<int:cat_pk>/<int:id>', cat_ptype_filter, name='cat_ptype_filter'),
    path('cat_clarification_filter/<int:cat_pk>/<int:id>/<int:clar_id>',
         cat_clarification_filter,
         name='cat_clarification_filter'),
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('', get_main_page, name='main_page'),
]