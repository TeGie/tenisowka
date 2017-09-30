from django.db import models
import datetime
from dateutil.relativedelta import relativedelta
from collections import Counter
from django.urls import reverse


__all__ = ('Player', 'Match', 'Event', 'Attendance')


class Player(models.Model):
    name = models.CharField(max_length=128, verbose_name='Imię i nazwisko')
    birth_date = models.DateField(null=True, blank=True, verbose_name='data urodzenia')
    adress = models.CharField(max_length=128, blank=True, verbose_name='adres')
    med_check_date = models.DateField(null=True, blank=True, verbose_name='data badania')
    licence_number = models.IntegerField(null=True, blank=True, verbose_name='nr licencji')
    elo_rating = models.SmallIntegerField(default=1200)

    class Meta:
        verbose_name = 'Zawodnik'
        verbose_name_plural = 'Zawodnicy'

    def __str__(self):
        return self.name

    def med_check(self):
        med_check_date = self.med_check_date
        med_check_span = relativedelta(datetime.date.today(), med_check_date)
        return {'med_check_span': med_check_span}

    def performance(self):
        wins_1, wins_2, win_list, loss_list = 0, 0, [], []
        match_1 = self.player_1.all()
        match_2 = self.player_2.all()
        if match_1 or match_2:
            for m in match_1:
                if m.result_pl_1 == 3:
                    wins_1 += 1
                    win_list.append(m.player_2.name)
                else:
                    loss_list.append(m.player_2.name)
            for m in match_2:
                if m.result_pl_2 == 3:
                    wins_2 += 1
                    win_list.append(m.player_1.name)
                else:
                    loss_list.append(m.player_1.name)
            success_rate = (round((wins_1 + wins_2) / (len(match_1) + len(match_2)) * 100, 2))
            failure_rate = 100 - success_rate
        else:
            success_rate = 'Brak pojedynków'
            failure_rate = 'Brak pojedynków'
        defeated = Counter(win_list).most_common(3)
        defeated_by = Counter(loss_list).most_common(3)
        return {'success_rate': success_rate,
                'failure_rate': failure_rate,
                'defeated': defeated,
                'defeated_by': defeated_by}


class Match(models.Model):
    RESULT = (
        (0, '0'),
        (1, '1'),
        (2, '2'),
        (3, '3'),
    )
    player_1 = models.ForeignKey('Player', related_name='player_1', null=True, verbose_name='zawodnik 1')
    player_2 = models.ForeignKey('Player', related_name='player_2', null=True, verbose_name='zawodnik 2')
    player_1_result = models.PositiveSmallIntegerField(choices=RESULT, default=0, verbose_name='wynik zawodnika 1')
    player_2_result = models.PositiveSmallIntegerField(choices=RESULT, default=0, verbose_name='wynik zawodnika 2')
    description = models.TextField(blank=True, null=True, verbose_name='opis')
    date = models.DateField(verbose_name='data')

    class Meta:
        verbose_name = 'Pojedynek'
        verbose_name_plural = 'Pojedynki'

    def __str__(self):
        return '{} - {} - {}'.format(self.player_1, self.player_2, self.date)

    def save(self, *args, **kwargs):
        try:
            player_1 = Player.objects.get(pk=self.player_1.pk)
            player_2 = Player.objects.get(pk=self.player_2.pk)
            player_1_elo = player_1.elo_rating
            player_2_elo = player_2.elo_rating
            expected_1 = 1 / (1 + 10 ** ((player_2_elo - player_1_elo) / 400))
            expected_2 = 1 / (1 + 10 ** ((player_1_elo - player_2_elo) / 400))
            if self.player_1_result == 3:
                player_1_new_elo = player_1.elo_rating + 32 * (1 - expected_1)
                player_2_new_elo = player_2.elo_rating + 32 * (0 - expected_2)
            else:
                player_1_new_elo = player_1.elo_rating + 32 * (0 - expected_2)
                player_2_new_elo = player_2.elo_rating + 32 * (1 - expected_1)
            player_1.elo_rating = player_1_new_elo
            player_2.elo_rating = player_2_new_elo
            player_1.save()
            player_2.save()
        except Exception as e:
            print(e)
        super(Match, self).save(*args, **kwargs)


class Event(models.Model):
    name = models.CharField(max_length=255, null=True, verbose_name='nazwa')
    description = models.TextField(blank=True, null=True, verbose_name='opis')
    start = models.DateTimeField(null=True)
    end = models.DateTimeField(null=True, verbose_name='koniec')

    class Meta:
        verbose_name = 'Wydarzenie'
        verbose_name_plural = 'Wydarzenia'

    def __str__(self):
        return self.name


class Attendance(models.Model):
    players = models.ManyToManyField(Player, verbose_name='Zawodnik')
    event = models.ForeignKey(Event, verbose_name='Wydarzenie')
    present = models.BooleanField()

    def get_absolute_url(self):
        return reverse ('event', kwargs={'pk': self.event.pk})