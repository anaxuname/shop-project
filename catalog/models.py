from django.conf import settings
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='наименование')
    description = models.CharField(max_length=150, verbose_name='описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='наименование')
    description = models.TextField(verbose_name='описание')
    image_preview = models.ImageField(upload_to='products/', verbose_name='изображение', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category')
    purchase_price = models.IntegerField(verbose_name='цена за покупку')
    data_create = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    data_last_change = models.DateTimeField(auto_now=True, verbose_name='дата последнего изменения')
    published = models.BooleanField(default=True, verbose_name='Опубликовано')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='авторизованый пользователь')
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        permissions = [
            (
                'work_with_products',
                'Can add and correct products'
            )
        ]


class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='version')
    version_number = models.IntegerField(verbose_name='версия продукта')
    version_name = models.CharField(max_length=100, verbose_name='название версии')
    active_version = models.BooleanField(verbose_name='признак текущей версии')
