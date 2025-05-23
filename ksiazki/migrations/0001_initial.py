# Generated by Django 5.2.1 on 2025-05-18 11:14

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ksiazka',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tytul', models.CharField(max_length=200)),
                ('autor', models.CharField(max_length=100)),
                ('opis', models.TextField()),
                ('cena', models.DecimalField(decimal_places=2, max_digits=6)),
                ('dostepna', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Wypozyczenie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_wypozyczenia', models.DateTimeField(auto_now_add=True)),
                ('data_zwrotu', models.DateTimeField(blank=True, null=True)),
                ('ksiazka', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ksiazki.ksiazka')),
                ('uzytkownik', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
