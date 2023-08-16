from django.http import HttpResponse
from django.shortcuts import render

from catalog.models import Product
from random import shuffle


# Create your views here.
def home(request):
    context = {
        'title': 'Каталог',
        'object_list': Product.objects.all(),
        'button': 'Перейти к товару'
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


def product(request, pk):

    context = {
        'object': Product.objects.get(pk=pk),
        'title': 'Товар',
        'button': 'В корзину'
    }
    return render(request, 'catalog/product.html', context)
