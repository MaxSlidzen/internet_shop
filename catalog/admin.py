from django.contrib import admin
from catalog.models import Product, Category, Message


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'price')
    list_filter = ('category',)
    search_fields = ('name', 'description',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Message)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'message')
