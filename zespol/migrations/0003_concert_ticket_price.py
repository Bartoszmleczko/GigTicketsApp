# Generated by Django 3.0 on 2020-01-03 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zespol', '0002_auto_20200103_1242'),
    ]

    operations = [
        migrations.AddField(
            model_name='concert',
            name='ticket_price',
            field=models.IntegerField(default=40, verbose_name='ticket_price'),
        ),
    ]
