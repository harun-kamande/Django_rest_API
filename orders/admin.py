from django.contrib import admin
from .models import Orders

# Register your models here.

@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer', 'order_date', 'order_amount', 'order_status']
    search_fields = ['customer__username', 'order_status']
    list_filter = ['order_status', 'order_date']