from django.db import models
print('hello world')
# Create your models here.


class Place(models.Model):
    title = models.CharField(max_length=200, primary_key=True)
    description_short = models.TextField('Краткое описание')
    description_long = models.TextField('Подробное описание')
    lat = models.FloatField('Широта')
    lon = models.FloatField('Долгота')

    def __str__(self):
        return self.title


class Image(models.Model):
    priority = models.CharField(max_length=1)
    title = models.CharField(max_length=200)
    photo = models.ImageField('Фото', upload_to='media')
    location = models.ForeignKey(
        Place,
        on_delete=models.CASCADE,
        verbose_name='Локация',
        related_name='location_photo'
    )
    def __str__(self):
        return self.title

    class Meta:
        ordering = ['priority']

