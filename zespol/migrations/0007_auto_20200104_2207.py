# Generated by Django 3.0 on 2020-01-04 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zespol', '0006_auto_20200104_2046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='first_name',
            field=models.CharField(max_length=30, verbose_name='imie'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='last_name',
            field=models.CharField(max_length=30, verbose_name='nazwisko'),
        ),
    ]
