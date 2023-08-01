from django.core.management import BaseCommand, call_command

from catalog.models import Product, Category
import json


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        Product.objects.all().delete()
        Category.objects.all().delete()
        # product_list = []
        # category_list = []
        # with open('catalog.json', 'r', encoding='utf-8') as f:
        #     data = json.load(f)
        #     for item in data:
        #         if item['model'] == 'catalog.category':
        #             category_list.append(Category(pk=item['pk'], **item['fields']))
        #
        #         С продуктами не работает из-за FK
        #         elif item['model'] == 'catalog.product':
        #             product_list.append(Product(pk=item['pk'], **item['fields']))
        #
        # Category.objects.bulk_create(category_list)
        # Product.objects.bulk_create(product_list)
        call_command('loaddata', 'catalog.json')