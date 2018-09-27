from django.contrib.auth.models import Permission, User
from django.db import models

class Annonser(models.Model):
    user = models.ForeignKey(User, default=1)
    tittel = models.CharField(max_length=150)
    dato = models.DateTimeField(auto_now=True)
    tags = models.CharField(max_length=100)
    stillinger = models.IntegerField()
    info = models.TextField(max_length=1000)

    def __str__(self):
        return self.tittel

class Emne(models.Model):
    emne = models.CharField(max_length=50)

    def __str__(self):
        return self.emne

class Annonse_emne(models.Model):
    annonse = models.ForeignKey(Annonser)
    emne = models.ForeignKey(Emne)



class Brukerinformasjon(models.Model):
    user = models.ForeignKey(User, default=1)
    erfaring = models.CharField(max_length=200)
    hjemmeside = models.URLField()
    om_meg = models.TextField(max_length=1000)

class Utviklere(models.Model):
    user = models.ForeignKey(User, default=1)
    tittel = models.CharField(max_length=150)
    dato = models.DateTimeField(auto_now=True)
    tags = models.CharField(max_length=100)
    info = models.TextField(max_length=1000)
    epost = models.EmailField(default='example@mail.com')


    def __str__(self):
        return self.tittel


class Søknader(models.Model):
    annonse = models.ForeignKey(Annonser, on_delete=models.CASCADE)
    søker = models.ForeignKey(User, default=1)
    dato = models.DateTimeField(auto_now=True)
    tekst = models.TextField(max_length=1000)
    epost = models.EmailField(default='example@mail.com')

    def __str__(self):
        return self.annonse