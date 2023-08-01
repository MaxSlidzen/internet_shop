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
    description = models.TextField(verbose_name='описание')
    image = models.ImageField(upload_to='products/', verbose_name='превью', **NULLABLE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='категория')
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='стоимость')
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True, verbose_name='создано')
    changed_at = models.DateTimeField(auto_now=True, auto_now_add=False, **NULLABLE, verbose_name='изменено')

    def __str__(self):
        return f'{self.name} - {self.description}. Стоимость {self.price} за 1 штуку.'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        ordering = ('name',)
