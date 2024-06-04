from django.core.paginator import Paginator
from django.shortcuts import render, get_list_or_404

from products.models import Products


def catalog(request, category_slug, page=1):
    if category_slug == 'all':
        products = Products.objects.all()
    else:
        products = get_list_or_404(Products.objects.filter(category__slug=category_slug))

    paginator = Paginator(products, 3)
    current_page = paginator.page(page)

    context = {
        'title': 'Home - Каталог',
        'products': current_page,
        'slug_url': category_slug,
    }
    return render(request, 'products/catalog.html', context)


def product_detail(request, product_slug):
    product_detail = Products.objects.get(slug=product_slug)
    context = {'product_detail': product_detail}
    return render(request, 'products/product_detail.html', context=context)
