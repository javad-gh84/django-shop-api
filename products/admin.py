from django.contrib import admin
from .models import Products


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ('title', 'Category', 'price', 'discount_price', 'count', 'created_at')
    list_filter = ('Category', 'created_at')
    search_fields = ('title', 'description')
    readonly_fields = ('created_at',)