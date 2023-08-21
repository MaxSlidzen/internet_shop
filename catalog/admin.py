from django.contrib import admin
from catalog.models import Product, ProductVersion, Category, Message


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'price')
    list_filter = ('category',)
    search_fields = ('name', 'description',)


@admin.register(ProductVersion)
class ProductVersion(admin.ModelAdmin):
    list_display = ('pk', 'name', 'version_number', 'product', 'is_active')
    list_filter = ('product',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'message')
