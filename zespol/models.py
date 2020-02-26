from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.


class Genre(models.Model):
    name = models.CharField("genre_name", max_length=30)

    class Meta:
        verbose_name = 'Gatunek'
        verbose_name_plural = 'Gatunki'

    def __unicode__(self):
        return self.name
    def __str__(self):
        return self.name

class Band(models.Model):
    name = models.CharField('band_name', max_length=50)
    image = models.ImageField("band_image", upload_to="icons/bands", blank=True)
    genre = models.ForeignKey(Genre,on_delete=models.CASCADE)
    class Meta:
        verbose_name="Zespol"
        verbose_name_plural="Zespoly"

    def __unicode__(self):
        return self.name
    def __str__(self):
        return self.name

class Club(models.Model):
    name = models.CharField("club_name", max_length=100)
    address = models.CharField("address", max_length=100)
    city = models.CharField("address", max_length=100,default='Rzeszów')
    image = models.ImageField("club_image", upload_to="icons/clubs", blank=True)
    normal_tickets = models.IntegerField("normal_tickets",default=100)

    class Meta:
        verbose_name="Klub"
        verbose_name_plural="Kluby"

    def __unicode__(self):
        return self.name
    def __str__(self):
        return self.name

class Concert(models.Model):
    name = models.CharField("concert_name", max_length=100)
    date = models.DateTimeField("concert_date")
    band = models.ForeignKey(Band,on_delete=models.CASCADE)
    club = models.ForeignKey(Club,on_delete=models.CASCADE)
    normal_tickets = models.IntegerField("normal_tickets",default=100)
    ticket_price = models.IntegerField("ticket_price", default=40)

    class Meta:
        verbose_name="Koncert"
        verbose_name_plural="Koncerty"

    def __unicode__(self):
        return self.name
    def __str__(self):
        return self.name
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    imie = models.CharField("imie", max_length=30)
    nazwisko = models.CharField("nazwisko", max_length=30)
    email = models.CharField("email", max_length=30)
    image = models.ImageField("profile_image", upload_to="profiles", blank=True)
    class Meta:
        verbose_name="Profil"
        verbose_name_plural="Profile"

    def __unicode__(self):
        return self.name


class Ticket(models.Model):
    concert = models.ForeignKey(Concert,on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile ,on_delete=models.CASCADE)
    is_bought = models.BooleanField("is_bought",default=False)
    class Meta:
        verbose_name="Bilet"
        verbose_name_plural="Bilety"

    def __unicode__(self):
        return self.concert.name



@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

