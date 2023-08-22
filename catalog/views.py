from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from pytils.translit import slugify

from catalog.forms import ProductForm, ProductVersionForm
from catalog.models import Product, Message, ProductVersion
from django.urls import reverse_lazy, reverse
from django.forms import inlineformset_factory


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

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        ProductVersionFormset = inlineformset_factory(Product, ProductVersion, form=ProductVersionForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = ProductVersionFormset(self.request.POST)
        else:
            context_data['formset'] = ProductVersionFormset()

        return context_data

    def form_valid(self, form):

        if form.is_valid():
            new_product = form.save()
            new_product.slug = slugify(new_product.name)
            new_product.save()
        formset = self.get_context_data()['formset']
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()

        return super().form_valid(form)


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product_list')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        ProductVersionFormset = inlineformset_factory(Product, ProductVersion, form=ProductVersionForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = ProductVersionFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = ProductVersionFormset(instance=self.object)

        return context_data

    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()

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


class ProductVersionListView(ListView):
    model = ProductVersion
