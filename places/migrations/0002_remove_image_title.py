# Generated by Django 4.0.6 on 2022-08-17 18:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='title',
        ),
    ]
