# Generated by Django 3.0 on 2020-01-03 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zespol', '0003_concert_ticket_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='is_bought',
            field=models.BooleanField(default=False, verbose_name='is_bought'),
        ),
    ]