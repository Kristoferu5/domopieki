from django.db import models

# Create your models here.

class Lekarz(models.Model):
    imie = models.CharField(max_length=20)
    nazwisko = models.CharField(max_length=50)
    specjalizacja = models.CharField(max_length=50)
    dane_kontaktowe = models.TextField(max_length=50, null=True)

    def __str__(self):
        return f'{self.imie} {self.nazwisko}'

class HistoriaLeczenia(models.Model):
    data = models.DateField()
    opis_problemu_zdrowotnego = models.CharField(max_length=255)
    zalecone_leczenie = models.CharField(max_length=255, null=True)
    pensjonariusz = models.ForeignKey('Pensjonariusz', on_delete=models.CASCADE, related_name='historie_leczenia')
    recepty = models.ManyToManyField('Recepty', blank=True, related_name='historie_leczenia')

    def __str__(self):
        return f'{self.data} {self.opis_problemu_zdrowotnego}'

class Pensjonariusz(models.Model):
    imie = models.CharField(max_length=20)
    nazwisko = models.CharField(max_length=50)
    data_urodzenia = models.DateField()
    plec = models.CharField(max_length=10)
    dane_kontaktowe = models.TextField(max_length=50, null=True)
    informacje_medyczne = models.CharField(max_length=255)
    #historia_leczenia = models.ForeignKey('HistoriaLeczenia', null=True, blank=True, on_delete=models.SET_NULL, related_name='pensjonariusze')

    def __str__(self):
        return f'{self.imie} {self.nazwisko}'


class Recepty(models.Model):
    data_wystawienia = models.DateField()
    zalecone_leki = models.TextField(max_length=255, null=True)
    lekarz = models.ForeignKey(Lekarz, on_delete=models.CASCADE)
    pensjonariusz = models.ForeignKey(Pensjonariusz, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.data_wystawienia} {self.zalecone_leki}'

