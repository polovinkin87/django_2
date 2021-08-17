from django.shortcuts import render
from basketapp.models import Basket
from mainapp.models import Product


def index(request):
    title = 'магазин'
    product = Product.objects.filter(is_deleted=False, category__is_deleted=False).select_related('category')[:3]
    context = {
        'title': title,
        'product': product,
    }
    return render(request, 'service/index.html', context)


def contacts(request):
    title = 'контакты'
    context = {
        'title': title
    }
    return render(request, 'service/contact.html', context)
