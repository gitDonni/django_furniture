from django.urls import path
from django.views.decorators.cache import cache_page

from main import views

app_name = 'main'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('about/', cache_page(60)(views.AboutView.as_view()), name='about'),
    path('payment_and_delivery/', cache_page(60)(views.PaymentView.as_view()), name='payment_and_delivery'),
    path('contact_info/', cache_page(60)(views.ContactInfoView.as_view()), name='contact_info'),
    ]
