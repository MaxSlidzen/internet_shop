from django.http import HttpResponse
from django.shortcuts import render

from catalog.models import Product
from random import shuffle


# Create your views here.
def home(request):
    context = {
        'title': 'Главная',
        'object_list': Product.objects.all(),
    }
    return render(request, 'catalog/home.html', context)


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'You have new message from {name}({phone}): {message}')

    context = {
        'title': 'Контакты'
    }
    return render(request, 'catalog/contacts.html', context)


# def catalog(request):
#
#     context = {
#         'object_list': Product.objects.all(),
#         'title': 'Каталог',
#     }
#     return render(request, 'catalog/catalog.html', context)


# def home(request):
#     product = Product.objects.all()
#     product_list.shuffle()
#
#     context = {
#         'object_list': product_list[:5],
#         'title': 'Главная',
#     }
#     return render(request, 'catalog/home.html', context)