from django.shortcuts import render


def create_orders(request):
    return render(request, 'orders/create_orders.html')

