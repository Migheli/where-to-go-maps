from django.db import models
print('hello world')
# Create your models here.


class Place(models.Model):
    title = models.CharField(max_length=200)
    description_short = models.TextField('Краткое описание')
    description_long = models.TextField('Подробное описание')
    lat = models.FloatField('Широта')
    lon = models.FloatField('Долгота')

    def __str__(self):
        return self.title
