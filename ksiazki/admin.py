from django.contrib import admin
from .models import Ksiazka, Wypozyczenie
from .models import StronaKsiazki

# Register your models here.

admin.site.register(Ksiazka)
admin.site.register(Wypozyczenie)
admin.site.register(StronaKsiazki)


