from django.shortcuts import render


def products(request):
    title = 'продукты | каталог'

    filter_menu = [
        {'filter': '*', 'name': 'All Products'},
        {'filter': '.new', 'name': 'Newest'},
        {'filter': '.low', 'name': 'Low Price'},
        {'filter': '.high', 'name': 'Hight Price'},
    ]

    context = {
        'title': title,
        'filter_menu': filter_menu,
    }

    return render(request=request, template_name='mainapp/products.html', context=context)
