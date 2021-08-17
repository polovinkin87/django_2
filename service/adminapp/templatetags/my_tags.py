from django import template
from django.conf import settings

register = template.Library()


def media_folder_products(string):
    if not string:
        string = 'product_images/default.jpeg'
    return f'{settings.MEDIA_URL}{string}'


register.filter('media_folder_products', media_folder_products)
