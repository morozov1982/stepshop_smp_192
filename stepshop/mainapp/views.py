from django.shortcuts import render, get_object_or_404

from mainapp.models import ProductCategory, Product


def products(request, pk=0):
    title = 'продукты | каталог'

    links_menu = ProductCategory.objects.all()

    context = {
        'title': title,
        'links_menu': links_menu,
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
