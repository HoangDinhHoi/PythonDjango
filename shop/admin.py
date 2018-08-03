"""docstrings for admin shop"""
from django.contrib import admin
from .models import Category, Product
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    """docstrings"""
    list_display = ['name', 'slug',]
    prepopulated_fields = {'slug': ('name',)}
    class Meta:
        model = Category
admin.site.register(Category, CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    """docstrings"""
    list_display = ['name', 'slug', 'category', 'price', 'stock', 'availble', 'created', 'updated',]
    list_filter = ['availble', 'created', 'updated', 'category',]
    list_editable = ['price', 'stock', 'availble',]
    prepopulated_fields = {'slug': ('name',)}

    class Meta:
        model = Product
        
admin.site.register(Product, ProductAdmin)
