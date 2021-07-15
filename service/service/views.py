from django.shortcuts import render
from mainapp.models import Product


def index(request):
    title = 'магазин'
    product = Product.objects.all()[:5]
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
