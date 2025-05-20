from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Ksiazka(models.Model):
    tytul = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    opis = models.TextField()
    cena = models.DecimalField(max_digits=6, decimal_places=2)
    dostepna = models.BooleanField(default=True)
    obrazek = models.ImageField(upload_to="okladki/", null=True, blank=True)
    tresc = models.TextField(null=True, blank=True, help_text="Wpisz treść książki tutaj")
    def czy_dostepna(self):
        return not Wypozyczenie.objects.filter(ksiazka=self, data_zwrotu__isnull=True).exists()

    class Meta:
        verbose_name = "Książka"
        verbose_name_plural = "Książki"

    def __str__(self):
        return self.tytul

class Wypozyczenie(models.Model):
    uzytkownik = models.ForeignKey(User, on_delete=models.CASCADE)
    ksiazka = models.ForeignKey(Ksiazka, on_delete=models.CASCADE)
    data_wypozyczenia = models.DateTimeField(auto_now_add=True)
    data_zwrotu = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name = "Wypozyczenie"
        verbose_name_plural = "Wypożyczenia"

    def __str__(self):
        return f"{self.uzytkownik.username} wypożyczył {self.ksiazka.tytul}"


class StronaKsiazki(models.Model):
    ksiazka = models.ForeignKey(Ksiazka, on_delete=models.CASCADE, related_name='strony')
    numer_strony = models.PositiveIntegerField()
    tresc = models.TextField()

    class Meta:
        verbose_name = "Strona książki"
        verbose_name_plural = "Strony książki"
        ordering = ['numer_strony']

    def __str__(self):
        return f"{self.ksiazka.tytul} - strona {self.numer_strony}"