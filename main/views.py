from django.shortcuts import render
from django.http import HttpResponse
from products.models import Categories


def index(request):
    categories = Categories.objects.all()
    context = {
        'title': 'Home - Главная',
        'content': 'Магазин мебели HOME',
        'categories': categories
    }
    return render(request, 'main/index.html', context)

def about(request):
    context = {
        'title': 'Home - О нас',
        'content': 'О нас',
        'text_on_page': 'Текст о том почему этот магазиг такой классный, и какой классный товар.'
    }
    return render(request, 'main/about.html', context)