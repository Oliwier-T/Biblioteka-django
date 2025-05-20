from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_ksiazek, name='lista_ksiazek'),
    path('baza/', views.baza, name='baza_strony'),
    path('dodaj/', views.dodaj_ksiazke, name='dodaj_ksiazke'),
    path('rejestracja/', views.rejestracja, name='register'),
    path('ksiazka/<int:pk>/usun/', views.usun_ksiazke, name='usun_ksiazke'),
    path('wypozycz/<int:pk>/', views.wypozycz_ksiazke, name='wypozycz_ksiazke'),
    path('wypozyczenia/', views.lista_wypozyczen, name='lista_wypozyczen'),
    path('wypozyczenia/cofnij/<int:pk>/', views.cofnij_wypozyczenie, name='cofnij_wypozyczenie'),
    path('ksiazka/<int:pk>/podglad/', views.podglad_ksiazki, name='podglad_ksiazki'),
    path('moja-ksiazka/', views.moja_ksiazka, name='moja_ksiazka'),
]