from django import forms
from .models import Suggestion

class SuggestionForm(forms.ModelForm):
    class Meta:
        model = Suggestion
        fields = ['nom_francais', 'nom_anglais', 'definition_FR', 'definition_EN', 'email']  # Ajout de 'definition_EN'
        labels = {
            'nom_francais': 'Nom Français',
            'nom_anglais': 'Nom Anglais',
            'definition_FR': 'Définition Française',
            'definition_EN': 'Définition Anglaise',  # Ajout du label
            'email': 'Votre Email',
        }
        widgets = {
            'nom_francais': forms.TextInput(attrs={'placeholder': 'Ex: Jeu vidéo'}),
            'nom_anglais': forms.TextInput(attrs={'placeholder': 'Ex: Video game'}),
            'definition_FR': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Définition en français'}),
            'definition_EN': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Définition en anglais'}),  # Ajout ici
            'email': forms.EmailInput(attrs={'placeholder': 'Votre adresse e-mail'}),
        }
