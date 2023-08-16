from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from catalog.models import Product, Message
from django.urls import reverse_lazy


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


class MessageCreateView(CreateView):
    model = Message
    fields = ['name', 'phone', 'message']
    template_name = 'catalog/contacts.html'
    success_url = reverse_lazy('catalog:contacts')
    extra_context = {
        'title': 'Контакты'
    }
