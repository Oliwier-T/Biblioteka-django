from django.shortcuts import render, redirect, get_object_or_404
from .models import Ksiazka, Wypozyczenie
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import KsiazkaForm, RejestracjaForm
from django.contrib import messages

# Create your views here.

def lista_ksiazek(request):
    ksiazki = Ksiazka.objects.all()
    return render(request, 'ksiazki/lista.html', {'ksiazki': ksiazki})

def baza(request):
    ksiazki = Ksiazka.objects.all()
    return render(request, 'ksiazki/base.html', {'ksiazki': ksiazki})



@user_passes_test(lambda u: u.is_superuser, login_url='lista_ksiazek')
def dodaj_ksiazke(request):
    if request.method == 'POST':
        form = KsiazkaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_ksiazek')
    else:
        form = KsiazkaForm()
    return render(request, 'ksiazki/dodaj_ksiazke.html', {'form': form})

def rejestracja(request):
    if request.method == "POST":
        form = RejestracjaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Konto zostało utworzone. Możesz się teraz zalogować.")
            return redirect('login')
    else:
        form = RejestracjaForm()
    return render(request, 'ksiazki/rejestracja.html', {'form': form})

@user_passes_test(lambda u: u.is_staff)
def usun_ksiazke(request, pk):
    ksiazka = get_object_or_404(Ksiazka, pk=pk)
    if request.method == 'POST':
        ksiazka.delete()
        return redirect('lista_ksiazek')

    return redirect('lista_ksiazek')
@login_required()
def wypozycz_ksiazke(request, pk):
    ksiazka = get_object_or_404(Ksiazka, pk=pk)


    aktywne = Wypozyczenie.objects.filter(uzytkownik=request.user, data_zwrotu__isnull=True).exists()
    if aktywne:
        messages.error(request, "Możesz wypożyczyć tylko jedną książkę na raz.")
        return redirect('lista_ksiazek')

    if not ksiazka.dostepna:
        messages.error(request, "Ta książka jest już wypożyczona.")
        return redirect('lista_ksiazek')

    ksiazka.dostepna = False
    ksiazka.save()

    Wypozyczenie.objects.create(ksiazka=ksiazka, uzytkownik=request.user)
    messages.success(request, f'Wypożyczyłeś książkę: {ksiazka.tytul}')
    return redirect('lista_ksiazek')

def lista_wypozyczen(request):
    wypozyczenia = Wypozyczenie.objects.select_related('ksiazka', 'uzytkownik').order_by('-data_wypozyczenia')
    return render(request, 'ksiazki/lista_wypozyczen.html', {'wypozyczenia': wypozyczenia})

@login_required
def cofnij_wypozyczenie(request, pk):
    wypozyczenie = get_object_or_404(Wypozyczenie, pk=pk)


    if request.user != wypozyczenie.uzytkownik and not request.user.is_staff:
        messages.error(request, "Nie masz uprawnień do cofnięcia tego wypożyczenia.")
        return redirect('lista_wypozyczen')


    ksiazka = wypozyczenie.ksiazka
    wypozyczenie.delete()
    ksiazka.dostepna = True
    ksiazka.save()

    messages.success(request, f'Cofnięto wypożyczenie książki: {ksiazka.tytul}')
    return redirect('lista_wypozyczen')
def podglad_ksiazki(request, pk):
    ksiazka = get_object_or_404(Ksiazka, pk=pk)

    wypozyczyl = Wypozyczenie.objects.filter(
        uzytkownik=request.user, ksiazka=ksiazka, data_zwrotu__isnull=True
    ).exists()

    if not wypozyczyl:
        messages.error(request, "Nie masz dostępu do tej książki.")
        return redirect('lista_ksiazek')

    strony = ksiazka.strony.all()
    return render(request, 'ksiazki/Moja_ksiazka.html', {'ksiazka': ksiazka, 'strony': strony})

@login_required
def moja_ksiazka(request):
    aktywne_wypozyczenie = Wypozyczenie.objects.filter(
        uzytkownik=request.user, data_zwrotu__isnull=True
    ).select_related('ksiazka').first()

    if not aktywne_wypozyczenie:
        return render(request, 'ksiazki/moja_ksiazka.html', {'brak': True})

    return render(request, 'ksiazki/moja_ksiazka.html', {
        'ksiazka': aktywne_wypozyczenie.ksiazka
    })