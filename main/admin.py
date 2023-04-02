from django.contrib import admin
from .models import Product, Catalog, Unit, Brand, ProductType, Clarification, Packing

admin.site.register(Product)
admin.site.register(Catalog)
admin.site.register(Unit)
admin.site.register(Brand)
admin.site.register(ProductType)
admin.site.register(Clarification)
admin.site.register(Packing)