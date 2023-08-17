from django.core.management import BaseCommand, call_command

from catalog.models import Product, Category, Message
from blog.models import Article


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        Product.objects.all().delete()
        Category.objects.all().delete()
        Message.objects.all().delete()
        Article.objects.all().delete()

        call_command('loaddata', 'catalog_data.json')
        call_command('loaddata', 'blog_data.json')