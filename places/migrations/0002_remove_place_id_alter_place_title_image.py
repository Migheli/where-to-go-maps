# Generated by Django 4.0.6 on 2022-08-01 20:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='place',
            name='id',
        ),
        migrations.AlterField(
            model_name='place',
            name='title',
            field=models.CharField(max_length=200, primary_key=True, serialize=False),
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('priority', models.CharField(max_length=1)),
                ('title', models.CharField(max_length=200)),
                ('photo', models.ImageField(upload_to='', verbose_name='Фото')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='location_photo', to='places.place', verbose_name='Локация')),
            ],
        ),
    ]
