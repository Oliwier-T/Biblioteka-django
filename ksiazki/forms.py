from django import forms
from .models import Ksiazka
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class KsiazkaForm(forms.ModelForm):
    class Meta:
        model = Ksiazka
        fields = ['tytul', 'autor', 'opis', 'cena', 'dostepna', 'obrazek', 'tresc']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['obrazek'].required = True
        self.fields['tresc'].required = True

        for field in self.fields.values():
            widget = field.widget
            if not isinstance(widget, forms.CheckboxInput) and not isinstance(widget, forms.ClearableFileInput):
                widget.attrs.update({'class': 'form-control'})
            elif isinstance(widget, forms.CheckboxInput):
                widget.attrs.update({'class': 'form-check-input'})
            else:
                widget.attrs.update({'class': 'form-control-file'})




class RejestracjaForm(UserCreationForm):
    email = forms.EmailField(required=False, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")