from django.shortcuts import render


def index(request):
    title = 'магазин'
    context = {
        'title': title
    }
    return render(request, 'service/index.html', context)


def contacts(request):
    title = 'контакты'
    context = {
        'title': title
    }
    return render(request, 'service/contact.html', context)
