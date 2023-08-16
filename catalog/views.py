from django.shortcuts import render
from django.views.generic import ListView, DetailView
from catalog.models import Product


class ProductListView(ListView):
    model = Product
    extra_context = {
        'title': 'Каталог',
        'button': 'Перейти к товару'
    }


class ProductDetailView(DetailView):
    model = Product
    extra_context = {
        'title': 'Товар',
        'button': 'В корзину'
    }


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
