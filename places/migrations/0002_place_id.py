# Generated by Django 4.0.6 on 2022-08-02 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='id',
            field=models.CharField(default=1, max_length=5),
            preserve_default=False,
        ),
    ]
