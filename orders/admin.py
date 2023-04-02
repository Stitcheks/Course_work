from django.contrib import admin
from .models import Contact, Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['packing']


class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemInline]
    list_display = ['id', 'first_name', 'last_name', 'email',
                    'phone_number', 'created', 'updated', 'paid']
    list_filter = ['paid', 'created', 'updated']


admin.site.register(Contact)
admin.site.register(Order, OrderAdmin)
