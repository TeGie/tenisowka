from .models import Match
from django.forms import ModelForm
from django.core.exceptions import ValidationError


class MatchForm(ModelForm):
    class Meta:
        model = Match
        fields = '__all__'

    def clean(self):
        cleaned_data = super(MatchForm, self).clean()
        player_1_result = cleaned_data.get('player_1_result')
        player_2_result = cleaned_data.get('player_2_result')
        if player_1_result is not None and player_2_result is not None:
            if not (player_1_result != 3 and player_2_result == 3 or player_1_result == 3 and player_2_result != 3):
                self.add_error(None, ValidationError('Wpisz poprawny wynik'))
