from django.shortcuts import render
from django.views.generic import ListView
from catalog.models import Product


class ProductListView(ListView):
    model = Product
    extra_context = {
        'title': 'Каталог',
        'button': 'Перейти к товару'
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


def product(request, pk):

    context = {
        'object': Product.objects.get(pk=pk),
        'title': 'Товар',
        'button': 'В корзину'
    }
    return render(request, 'catalog/product.html', context)
