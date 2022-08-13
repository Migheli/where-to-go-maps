from django.db import models
from tinymce.models import HTMLField

# Create your models here


class Place(models.Model):
    id = models.BigAutoField('ID локации', primary_key=True)
    title = models.CharField('Название локации', max_length=200, unique=True)
    description_short = models.TextField('Краткое описание')
    description_long = HTMLField('Подробное описание')
    lat = models.FloatField('Широта')
    lon = models.FloatField('Долгота')

    class Meta:
        verbose_name = 'Локация'
        verbose_name_plural = 'Локации'

    def __str__(self):
        return self.title


class Image(models.Model):
    priority = models.PositiveIntegerField(
        default=0,
        blank=False,
        null=False,
        verbose_name='Приоритет'
    )
    title = models.CharField('Название файла', max_length=200)
    photo = models.ImageField('Фото', upload_to='media')
    location = models.ForeignKey(
        Place,
        on_delete=models.CASCADE,
        verbose_name='Локация',
        related_name='location_photo'
    )

    class Meta:
        ordering = ['priority']
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'

    def __str__(self):
        return self.title
