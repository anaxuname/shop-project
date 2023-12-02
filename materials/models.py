from django.db import models


class Material(models.Model):
    title = models.CharField(max_length=100, verbose_name='заголовок')
    slug = models.CharField(max_length=255, unique=True, db_index=True, verbose_name="URL") #(реализовать через CharField)
    body = models.TextField(verbose_name='содержимое')
    image_preview = models.ImageField(upload_to='material/', verbose_name='изображение', null=True, blank=True)
    data_create = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    is_public = models.BooleanField(verbose_name='признак публикации', default=True)
    count_view = models.Count(verbose_name='количество просмотров')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'материал'
        verbose_name_plural = 'материалы'