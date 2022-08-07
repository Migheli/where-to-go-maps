from django.db import models
from tinymce.models import HTMLField


print('hello world')
# Create your models here.



class Place(models.Model):
    id = models.CharField(max_length=5)
    title = models.CharField(max_length=200, primary_key=True)
    description_short = models.TextField('Краткое описание')
    description_long = HTMLField('Подробное описание')
    lat = models.FloatField('Широта')
    lon = models.FloatField('Долгота')

    def __str__(self):
        return self.title


class Image(models.Model):
    inline_customizable_order = models.PositiveIntegerField(
        default=0,
        blank=False,
        null=False,
        verbose_name='Приоритет при отображении'
    )
    title = models.CharField(max_length=200)
    photo = models.ImageField('Фото', upload_to='media')
    location = models.ForeignKey(
        Place,
        on_delete=models.CASCADE,
        verbose_name='Локация',
        related_name='location_photo'
    )


    class Meta:
        ordering = ['inline_customizable_order']

    def __str__(self):
        return self.title

