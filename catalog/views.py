from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from pytils.translit import slugify

from catalog.forms import ProductForm
from catalog.models import Product, Message
from django.urls import reverse_lazy, reverse


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


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product_list')

    def form_valid(self, form):
        if form.is_valid():
            new_product = form.save()
            new_product.slug = slugify(new_product.name)
            new_product.save()

        return super().form_valid(form)


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product_list')

    def form_valid(self, form):
        if form.is_valid():
            new_product = form.save()
            new_product.slug = slugify(new_product.name)
            new_product.save()

        return super().form_valid(form)


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:product_list')


class MessageCreateView(CreateView):
    model = Message
    fields = ['name', 'phone', 'message']
    template_name = 'catalog/contacts.html'
    success_url = reverse_lazy('catalog:contacts')
    extra_context = {
        'title': 'Контакты'
    }
