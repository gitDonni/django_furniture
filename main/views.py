from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from .models import About, Payment, ContactInfo
from products.models import Categories


class IndexView(TemplateView):
    template_name = 'main/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Home - Главная'
        context['content'] = 'Наши преимущества'
        return context


class AboutView(TemplateView):
    template_name = 'main/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        about = About.objects.first()
        if about:
            context['title'] = about.title
            context['content'] = about.content
            context['text_on_page'] = about.text_on_page
        else:
            context['title'] = 'Страница не найдена'
            context['content'] = 'Контент не найден'
            context['text_on_page'] = ''
        return context


class PaymentView(TemplateView):
    template_name = 'main/payment_and_delivery.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        payment = Payment.objects.first()
        context['title'] = payment.title
        context['content'] = payment.content
        context['text_on_page'] = payment.text_on_page
        return context


class ContactInfoView(TemplateView):
    template_name = 'main/contact_info.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        contacts = ContactInfo.objects.first()
        context['title'] = contacts.title
        context['content'] = contacts.content
        context['text_on_page'] = contacts.text_on_page
        context['phone'] = contacts.phone
        context['address'] = contacts.address
        context['email'] = contacts.email
        context['facebook'] = contacts.facebook
        context['instagram'] = contacts.instagram
        context['vk'] = contacts.vk
        return context

# def index(request):
#     context = {
#         'title': 'Home - Главная',
#         'content': 'Магазин мебели HOME',
#     }
#     return render(request, 'main/index.html', context)


# def about(request):
#     context = {
#         'title': 'Home - О нас',
#         'content': 'О нас',
#         'text_on_page': 'Текст о том почему этот магазиг такой классный, и какой классный товар.'
#     }
#     return render(request, 'main/about.html', context)