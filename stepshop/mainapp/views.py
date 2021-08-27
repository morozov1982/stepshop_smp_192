from django.shortcuts import render, get_object_or_404

from basketapp.models import Basket
from mainapp.models import ProductCategory, Product


def get_basket(request):
    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)
    return basket


def products(request, pk=0):
    title = 'продукты | каталог'

    links_menu = ProductCategory.objects.all()

    context = {
        'title': title,
        'links_menu': links_menu,
        'basket': get_basket(request),
    }

    if pk == 0:
        products = Product.objects.all().order_by('price')
        category = {'name': 'все'}
    else:
        category = get_object_or_404(ProductCategory, pk=pk)
        products = Product.objects.filter(category__pk=pk).order_by('price')

    context['category'] = category
    context['products'] = products

    return render(request=request, template_name='mainapp/products.html', context=context)


def product(request, pk):
    title = 'продукт'

    links_menu = ProductCategory.objects.all()
    product = get_object_or_404(Product, pk=pk)

    context = {
        'title': title,
        'links_menu': links_menu,
        'product': product,
        'basket': get_basket(request),
    }

    return render(request=request, template_name='mainapp/product.html', context=context)
