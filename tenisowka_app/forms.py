from django import forms
from .models import Pojedynek


class DodajPojedynekForm(forms.ModelForm):

    class Meta:
        model = Pojedynek
        fields = '__all__'
        widgets = {
            'set_1_zaw_1': forms.NumberInput(attrs={'class': 'wynik1'}),
            'set_2_zaw_1': forms.NumberInput(attrs={'class': 'wynik1'}),
            'set_3_zaw_1': forms.NumberInput(attrs={'class': 'wynik1'}),
            'set_4_zaw_1': forms.NumberInput(attrs={'class': 'wynik1'}),
            'set_5_zaw_1': forms.NumberInput(attrs={'class': 'wynik1'}),
            'set_1_zaw_2': forms.NumberInput(attrs={'class': 'wynik2'}),
            'set_2_zaw_2': forms.NumberInput(attrs={'class': 'wynik2'}),
            'set_3_zaw_2': forms.NumberInput(attrs={'class': 'wynik2'}),
            'set_4_zaw_2': forms.NumberInput(attrs={'class': 'wynik2'}),
            'set_5_zaw_2': forms.NumberInput(attrs={'class': 'wynik2'}),
        }
