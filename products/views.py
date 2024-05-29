from django.shortcuts import render

from products.models import Products


def catalog(request):
    products = Products.objects.all()
    context = {
        'title': 'Home - Каталог',
        'products': products,
    }
    return render(request, 'products/catalog.html', context)


def product_detail(request):
    return render(request, 'products/product_detail.html')
