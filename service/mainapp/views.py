from django.shortcuts import render
from mainapp.models import ProductCategory, Product


def products(request):
    title = 'продукты/каталог'
    product = Product.objects.all()[:5]
    category = ProductCategory.objects.all()[:5]
    context = {
        'title': title,
        'category': category,
        'product': product,
    }
    return render(request, 'mainapp/products.html', context)
