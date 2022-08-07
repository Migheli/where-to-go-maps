# Generated by Django 4.0.6 on 2022-08-07 10:20

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.CharField(max_length=5)),
                ('title', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('description_short', models.TextField(verbose_name='Краткое описание')),
                ('description_long', tinymce.models.HTMLField(verbose_name='Подробное описание')),
                ('lat', models.FloatField(verbose_name='Широта')),
                ('lon', models.FloatField(verbose_name='Долгота')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inline_customizable_priority', models.PositiveIntegerField(default=0, verbose_name='Приоритет при отображении')),
                ('title', models.CharField(max_length=200)),
                ('photo', models.ImageField(upload_to='media', verbose_name='Фото')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='location_photo', to='places.place', verbose_name='Локация')),
            ],
            options={
                'ordering': ['inline_customizable_priority'],
            },
        ),
    ]