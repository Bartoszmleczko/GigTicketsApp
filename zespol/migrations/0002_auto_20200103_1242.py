# Generated by Django 3.0 on 2020-01-03 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zespol', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='ticket_type',
        ),
        migrations.AddField(
            model_name='club',
            name='city',
            field=models.CharField(default='Rzeszów', max_length=100, verbose_name='address'),
        ),
        migrations.AddField(
            model_name='club',
            name='normal_tickets',
            field=models.IntegerField(default=100, verbose_name='normal_tickets'),
        ),
        migrations.AddField(
            model_name='concert',
            name='normal_tickets',
            field=models.IntegerField(default=100, verbose_name='normal_tickets'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='email',
            field=models.CharField(max_length=30, verbose_name='email'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='first_name',
            field=models.CharField(max_length=30, verbose_name='first_name'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='last_name',
            field=models.CharField(max_length=30, verbose_name='last_name'),
        ),
    ]