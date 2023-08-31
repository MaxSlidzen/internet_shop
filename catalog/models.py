from django.conf import settings
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='категория')
    description = models.TextField(verbose_name='описание')

    def __str__(self):
        return f'{self.name}, {self.description}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ('name',)


class Product(models.Model):
    name = models.CharField(max_length=50, verbose_name='наименование')
    slug = models.CharField(max_length=150, verbose_name='slug', **NULLABLE)
    description = models.TextField(verbose_name='описание')
    image = models.ImageField(upload_to='products/', verbose_name='превью', **NULLABLE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='категория')
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='стоимость')
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True, verbose_name='создано')
    changed_at = models.DateTimeField(auto_now=True, auto_now_add=False, **NULLABLE, verbose_name='изменено')

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, **NULLABLE, verbose_name='автор')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        ordering = ('name',)


class ProductVersion(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='продукт')
    version_number = models.CharField(max_length=10, verbose_name='версия')
    name = models.CharField(max_length=50, verbose_name='наименование')
    is_active = models.BooleanField(default=False, verbose_name='активность')

    def __str__(self):
        return f'{self.name} ({self.version_number})'

    class Meta:
        verbose_name = 'версия продукта'
        verbose_name_plural = 'версии продукта'


class Message(models.Model):
    name = models.CharField(max_length=50, verbose_name='имя')
    phone = models.CharField(max_length=10, verbose_name='телефон')
    message = models.TextField(verbose_name='сообщение')

    def __str__(self):
        return f'Cообщение от {self.name} ({self.phone})'

    class Meta:
        verbose_name = 'сообщение'
        verbose_name_plural = 'сообщения'
