from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='наименование')
    description = models.CharField(max_length=150, verbose_name='описание')
    image_preview = models.ImageField(upload_to='products/',verbose_name='изображение')
    category = models.CharField(max_length=100, verbose_name='категория')
    purchase_price = models.IntegerField(verbose_name='цена за покупку')
    data_create = models.DateField(verbose_name='дата создания')
    data_last_change = models.DateField(verbose_name='дата последнего изменения')

    def __str__(self):
        return f'{self.name}, {self.description}, {self.category}, {self.purchase_price}, {self.data_create}, {self.data_last_change}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='наименование')
    description = models.CharField(max_length=150, verbose_name='описание')

    def __str__(self):
        return f'{self.name} : {self.description}'