from django.contrib import admin

from blog.models import Article


@admin.register(Article)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'created', 'is_published',)
    search_fields = ('title', 'content',)
