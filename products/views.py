from django.core.paginator import Paginator
from django.shortcuts import render, get_list_or_404

from products.models import Products
from products.utils import q_search


def catalog(request, category_slug=None):
    page = request.GET.get('page', 1)
    on_sale = request.GET.get('on_sale', None)
    order_by = request.GET.get('order_by', None)
    query = request.GET.get('q', None)
    if category_slug == 'all':
        products = Products.objects.all()
    elif query:
        products = q_search(query)
    else:
        products = get_list_or_404(Products.objects.filter(category__slug=category_slug))

    if on_sale:
        products = products.filter(discount__gt=0)

    if order_by and order_by != "default":
        products = products.order_by(order_by)

    paginator = Paginator(products, 3)
    current_page = paginator.page(int(page))

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
