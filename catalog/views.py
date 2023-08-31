from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import MultipleObjectsReturned
from django.shortcuts import redirect
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


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    login_url = reverse_lazy('users:login')

    def get_success_url(self):
        button = self.request.POST.get('button')

        # Обработка данных в зависимости от нажатой кнопки
        if button == 'save':
            pk = self.get_context_data()['object'].pk
            slug = self.get_context_data()['object'].slug
            return reverse('catalog:product_update', args=[pk, slug])

        return reverse_lazy('catalog:product_list')

    def form_valid(self, form):
        if form.is_valid():
            new_product = form.save()
            new_product.slug = slugify(new_product.name)
            new_product.save()

        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    login_url = reverse_lazy('users:login')

    def get_success_url(self):
        # Обработка данных в зависимости от нажатой кнопки
        button = self.request.POST.get('button')
        if button == 'save_n_back':
            return reverse('catalog:product_detail', args=[self.kwargs.get('pk'), self.kwargs.get('slug')])

        return reverse('catalog:product_update', args=[self.kwargs.get('pk'), self.kwargs.get('slug')])

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


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:product_list')
    login_url = reverse_lazy('users:login')


class MessageCreateView(CreateView):
    model = Message
    fields = ['name', 'phone', 'message']
    template_name = 'catalog/contacts.html'
    success_url = reverse_lazy('catalog:contacts')
    extra_context = {
        'title': 'Контакты'
    }


@login_required(login_url=reverse_lazy('users:login'))
def choose_version(request, pk, version_id):

    product = Product.objects.get(pk=pk)

    try:
        active_version = ProductVersion.objects.get(product_id=product.pk, is_active=True)

    # Возникает, если с помощью админки или из-за бага на момент операции установлено более 1 активной версии.
    except MultipleObjectsReturned:
        print('Получено больше 1 текущей активной версиии. Выбранная версия установлена единственной активной.')
        all_versions = ProductVersion.objects.filter(product_id=product.pk)
        # Меняем активность всех версий на False
        for version in all_versions:
            version.is_active = False
            version.save()
        # Если пользователь убирает активную версию полностью, то происходит обновление страницы с новыми данными
        if version_id == '0':
            return redirect(reverse('catalog:product_update', args=[product.pk, product.slug]))
        # Установка активности выбранной пользователем версии
        else:
            choosen_version = ProductVersion.objects.get(id=int(version_id))
            choosen_version.is_active = True
            choosen_version.save()

    # Возникает, если текущая активная версия не установлена.
    except ProductVersion.DoesNotExist:
        # Изменение активной версии на ту же самую
        if version_id == '0':
            return redirect(reverse('catalog:product_update', args=[product.pk, product.slug]))
        else:
            choosen_version = ProductVersion.objects.get(id=int(version_id))
            choosen_version.is_active = True
            choosen_version.save()

    else:
        active_version.is_active = False
        active_version.save()
        if version_id != '0':
            choosen_version = ProductVersion.objects.get(id=int(version_id))
            choosen_version.is_active = True
            choosen_version.save()



    return redirect(reverse('catalog:product_update', args=[product.pk, product.slug]))
