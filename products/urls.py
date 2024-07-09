from django.urls import path

from products import views

app_name = 'products'

urlpatterns = [
    path('search/', views.catalog, name='search'),
    path('<slug:category_slug>/', views.catalog, name='index'),
    path('product_detail/<slug:product_detail_slug>/', views.product_detail, name='product_detail'),
    ]
