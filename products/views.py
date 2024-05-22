from django.shortcuts import render

def catalog(request):
    return render(request, 'products/catalog.html')

def product_detail(request):
    return render(request, 'products/product_detail.html')
