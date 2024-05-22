from django.urls import path

from products import views

app_name = 'products'

urlpatterns = [
    path('', views.catalog, name='index'),
    path('product_detail/', views.product_detail, name='product_detail'),
    ]
