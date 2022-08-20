from django.db import models
from tinymce.models import HTMLField
from pathlib import Path

# Create your models here


class Place(models.Model):
    title = models.CharField('Название локации', max_length=200, unique=True)
    description_short = models.TextField('Краткое описание', blank=True)
    description_long = HTMLField('Подробное описание', blank=True)
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
        verbose_name='Приоритет'
    )
    photo = models.ImageField('Фото', upload_to='media')
    location = models.ForeignKey(
        Place,
        on_delete=models.CASCADE,
        verbose_name='Локация',
        related_name='photos'
    )

    class Meta:
        ordering = ['priority']
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'

    def __str__(self):
        return Path(self.photo.name).name
