from django.shortcuts import render


def main(request):
    context = {
        'title': 'Магазин',
    }
    return render(request, 'mainapp/index.html', context)


def products(request):
    # links_menu = {
    #     {'href': 'products_all', 'name': 'все предложения'},
    #     {'href': 'products_clothes', 'name': 'Интернет магазины одежды'},
    #     {'href': 'products_another', 'name': 'Остальные интернет магазины'},
    # }
    context = {
        'title': 'Магазины',
    #     'links_menu': links_menu
    }
    return render(request, 'mainapp/products.html', context)


def products_all(request):
    links_menu = {
        {'href': 'products_all', 'name': 'все предложения', 'img': ''},
        {'href': 'products_clothes', 'name': 'Интернет магазины одежды'},
        {'href': 'products_another', 'name': 'Остальные интернет магазины'},
    }
    context = {
        'title': 'Все Магазины',
        'links_menu': links_menu
    }
    return render(request, 'mainapp/products.html', context)


def products_clothes(request):
    context = {
        'title': 'Магазины одежды',
    }
    return render(request, 'mainapp/products.html', context)


def products_another(request):
    context = {
        'title': 'Другие магазины',
    }
    return render(request, 'mainapp/products.html', context)


def contact(request):
    context = {
        'title': 'Контакты',
    }
    return render(request, 'mainapp/contact.html', context)
