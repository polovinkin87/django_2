from django.core.management.base import BaseCommand
import os
import json
from authapp.models import ShopUser
from mainapp.models import Product, ProductCategory

JSON_PATH = 'mainapp/jsons'


def load_from_json(file_name):
    with open(os.path.join(JSON_PATH, file_name + '.json'), 'r', encoding='UTF-8') as file:
        return json.load(file)


class Command(BaseCommand):
    def handle(self, *args, **options):
        categories = load_from_json('categories')

        ProductCategory.objects.all().delete()
        for category in categories:
            new_category = ProductCategory(**category)
            new_category.save()

        products = load_from_json('products')

        Product.objects.all().delete()
        for product in products:
            category_name = product['category']
            _category = ProductCategory.objects.get(name=category_name)
            product['category'] = _category
            new_category = Product(**product)
            new_category.save()

        super_user = ShopUser.objects.create_superuser('sysadmin', 'admin@mail.ru', 'qwerty1234', age='34')
