Biblioteka – Wypożyczalnia książek(Django)

Prosta aplikacja Django, która imituje wypożyczalnię książek (bibliotekę).  
Dla użytkowników umożliwia wyszukiwanie, a następnie wypożyczanie i czytanie książek.  
Administratorzy mają bardzo prostą obsługę dodawania i usuwania nowych książek.



Sposób uruchomienia:

1.Sklonowanie repozytorium:
git clone https://github.com/Oliwier-T/Biblioteka-django.git
cd Biblioteka-django

2.Utwórz i aktywuj wirtualne środowisko:
python -m venv venv
venv\Scripts\activate

3.Zainstalowanie zależności:
pip install -r requirements.txt

4.Wykonanie migracji:
python manage.py migrate

5.Załadowanie danych testowych z ksiazki.json:
python manage.py loaddata ksiazki.json

6.Odpalenie serwera:
python manage.py runserver
