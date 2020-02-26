# Generated by Django 3.0 on 2019-12-24 13:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Band',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='band_name')),
                ('image', models.ImageField(blank=True, upload_to='icons/bands', verbose_name='band_image')),
            ],
            options={
                'verbose_name': 'Zespol',
                'verbose_name_plural': 'Zespoly',
            },
        ),
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='club_name')),
                ('address', models.CharField(max_length=100, verbose_name='address')),
                ('image', models.ImageField(blank=True, upload_to='icons/clubs', verbose_name='club_image')),
            ],
            options={
                'verbose_name': 'Klub',
                'verbose_name_plural': 'Kluby',
            },
        ),
        migrations.CreateModel(
            name='Concert',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='concert_name')),
                ('date', models.DateTimeField(verbose_name='concert_date')),
                ('band', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zespol.Band')),
                ('club', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zespol.Club')),
            ],
            options={
                'verbose_name': 'Koncert',
                'verbose_name_plural': 'Koncerty',
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='genre_name')),
            ],
            options={
                'verbose_name': 'Gatunek',
                'verbose_name_plural': 'Gatunki',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=25, verbose_name='first_name')),
                ('last_name', models.CharField(max_length=25, verbose_name='last_name')),
                ('email', models.CharField(max_length=25, verbose_name='email')),
                ('image', models.ImageField(blank=True, upload_to='profiles', verbose_name='profile_image')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Profil',
                'verbose_name_plural': 'Profile',
            },
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticket_type', models.BooleanField(default=True)),
                ('concert', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zespol.Concert')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zespol.Profile')),
            ],
            options={
                'verbose_name': 'Bilet',
                'verbose_name_plural': 'Bilety',
            },
        ),
        migrations.AddField(
            model_name='band',
            name='genre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zespol.Genre'),
        ),
    ]