from django import forms
from django.conf import settings

class PersonForm(forms.Form):
    name = forms.CharField(
        max_length=200,
        required=True,
        strip=True,
        min_length=2,
        widget=forms.TextInput(
            attrs={
                'type':'text'
            }
        )
        
    )
    age = forms.IntegerField(
        required=True,
        widget=forms.NumberInput(
            attrs={
                'type':'number'
            }
        )
    )
    sex = forms.ChoiceField(
        required=True,
        choices=[(x,y) for (x,y) in settings.SEXE],
        widget=forms.Select(
            attrs={
                'type':'select'
            }
        )
    )
    country = forms.ChoiceField(
        required=True,
        choices=[(x,y) for (x,y) in settings.COUNTRIES],
        widget=forms.Select(
            attrs={
                'type':'select'
            }
        )
    )

class ProduitForm(forms.Form):
    name = forms.CharField(
        max_length=200,
        required=True,
        strip=True,
        min_length=2,
        widget=forms.TextInput(
            attrs={
                'type':'text'
            }
        )   
    )
    country = forms.ChoiceField(
        required=True,
        choices=[(x,y) for (x,y) in settings.COUNTRIES],
        widget=forms.Select(
            attrs={
                'type':'select'
            }
        )
    )
    price = forms.IntegerField(
        required=True,
        widget=forms.NumberInput(
            attrs={
                'type':'number'
            }
        )
    )

class MagasinForm(forms.Form):
    name = forms.CharField(
        max_length=200,
        required=True,
        strip=True,
        min_length=2,
        widget=forms.TextInput(
            attrs={
                'type':'text'
            }
        )   
    )
    country = forms.ChoiceField(
        required=True,
        choices=[(x,y) for (x,y) in settings.COUNTRIES],
        widget=forms.Select(
            attrs={
                'type':'select'
            }
        )
    )

class ProfileMagasinForm(forms.Form):
    email=forms.EmailField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'type':'text'
            }
        )
    )
    phone = forms.CharField(
        max_length=20,
        required=True,
        strip=True,
        min_length=2,
        widget=forms.TextInput(
            attrs={
                'type':'text'
            }
        )   
    )
    name = forms.CharField(
        max_length=200,
        required=True,
        strip=True,
        min_length=2,
        widget=forms.TextInput(
            attrs={
                'type':'text'
            }
        )   
    )
    country = forms.ChoiceField(
        required=True,
        choices=[(x,y) for (x,y) in settings.COUNTRIES],
        widget=forms.Select(
            attrs={
                'type':'select'
            }
        )
    )