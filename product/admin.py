from django.contrib import admin
from .models import Product,Category
# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price', 'stock', 'created_at']
    search_fields = ['name']
    list_filter = ['created_at']

admin.site.register(Category)