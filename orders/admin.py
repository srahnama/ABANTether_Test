from django.contrib import admin
from .models import Order

@admin.register(Order)

class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_id', 'currency', 'amount', 'price', 'exchange_order_id')


admin.site.site_header = 'Cryptocurrency Order Admin'
admin.site.site_title = 'Cryptocurrency Order Admin'
admin.site.index_title = 'Manage Cryptocurrency Orders'