from django.shortcuts import render
from mainapp.models import Product

from mainapp.views import get_basket


def index(request):
    title = 'магазин'

    products = Product.objects.all()  # [:4]

    context = {
        'title': title,
        'products': products,
        'basket': get_basket(request),
    }

    return render(request, 'stepshop/index.html', context=context)


def contacts(request):
    title = 'контакты'

    context = {
        'title': title,
        'basket': get_basket(request),
    }

    return render(request, 'stepshop/contact.html', context=context)


def about(request):
    title = 'о нас'

    context = {
        'title': title,
        'basket': get_basket(request),
    }

    return render(request, 'stepshop/about.html', context=context)
