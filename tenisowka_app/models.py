from django.db import models
import datetime
from dateutil.relativedelta import relativedelta
from collections import Counter


__all__ = ('Zawodnik', 'Pojedynek', 'Wydarzenie')


class Zawodnik(models.Model):
    imie = models.CharField(max_length=128, verbose_name='Imię i nazwisko')
    data_urodzenia = models.DateField(null=True, blank=True)
    adres = models.CharField(max_length=128, blank=True)
    data_badania = models.DateField(null=True, blank=True)
    nr_licencji = models.IntegerField(null=True, blank=True)
    elo_rating = models.IntegerField(default=1200)

    class Meta:
        verbose_name = 'Zawodnik'
        verbose_name_plural = 'Zawodnicy'

    def __str__(self):
        return self.imie

    def badanie(self):
        data_badania = self.data_badania
        czas = relativedelta(datetime.date.today(), data_badania)
        return {'czas': czas}

    def performance(self):
        wins_1, wins_2, win_arr, loss_arr = 0, 0, [], []
        pojedynek_1 = self.zawodnik_1.all()
        pojedynek_2 = self.zawodnik_2.all()
        if pojedynek_1 or pojedynek_2:
            for p in pojedynek_1:
                if p.wynik_zaw_1 == 3:
                    wins_1 += 1
                    win_arr.append(p.zawodnik_2.imie)
                else:
                    loss_arr.append(p.zawodnik_2.imie)
            for p in pojedynek_2:
                if p.wynik_zaw_2 == 3:
                    wins_2 += 1
                    win_arr.append(p.zawodnik_1.imie)
                else:
                    loss_arr.append(p.zawodnik_1.imie)
            success = (round((wins_1 + wins_2) / (len(pojedynek_1) + len(pojedynek_2)) * 100, 2))
            failure = 100 - success
        else:
            success = 'Brak pojedynków'
            failure = 'Brak pojedynków'
        win = Counter(win_arr).most_common(3)
        loss = Counter(loss_arr).most_common(3)
        return {'success': success,
                'failure': failure,
                'win': win,
                'loss': loss}


class Pojedynek(models.Model):
    zawodnik_1 = models.ForeignKey('Zawodnik', related_name='zawodnik_1', null=True)
    zawodnik_2 = models.ForeignKey('Zawodnik', related_name='zawodnik_2', null=True)
    set_1_zaw_1 = models.SmallIntegerField(default=0)
    set_2_zaw_1 = models.SmallIntegerField(default=0)
    set_3_zaw_1 = models.SmallIntegerField(default=0)
    set_4_zaw_1 = models.SmallIntegerField(default=0)
    set_5_zaw_1 = models.SmallIntegerField(default=0)
    set_1_zaw_2 = models.SmallIntegerField(default=0)
    set_2_zaw_2 = models.SmallIntegerField(default=0)
    set_3_zaw_2 = models.SmallIntegerField(default=0)
    set_4_zaw_2 = models.SmallIntegerField(default=0)
    set_5_zaw_2 = models.SmallIntegerField(default=0)
    wynik_zaw_1 = models.SmallIntegerField(default=0)
    wynik_zaw_2 = models.SmallIntegerField(default=0)
    data = models.DateField()

    class Meta:
        verbose_name = 'Pojedynek'
        verbose_name_plural = 'Pojedynki'

    def __str__(self):
        return '{} - {} - {}'.format(self.zawodnik_1, self.zawodnik_2, self.data)


    def save(self,*args,**kwargs):
        try:
            zawodnik_1 = Zawodnik.objects.get(pk=self.zawodnik_1.pk)
            zawodnik_2 = Zawodnik.objects.get(pk=self.zawodnik_2.pk)
            rating_1 = zawodnik_1.elo_rating
            rating_2 = zawodnik_2.elo_rating
            expected_1 = 1 / (1 + 10 ** ((rating_2 - rating_1) / 400))
            expected_2 = 1 / (1 + 10 ** ((rating_1 - rating_2) / 400))
            if self.wynik_zaw_1 == 3:
                new_zawodnik_1_elo = zawodnik_1.elo_rating + 32 * (1 - expected_1)
                new_zawodnik_2_elo = zawodnik_2.elo_rating + 32 * (0 - expected_2)
            else:
                new_zawodnik_1_elo = zawodnik_1.elo_rating + 32 * (0 - expected_2)
                new_zawodnik_2_elo = zawodnik_2.elo_rating + 32 * (1 - expected_1)
            zawodnik_1.elo_rating = new_zawodnik_1_elo
            zawodnik_2.elo_rating = new_zawodnik_2_elo
            zawodnik_1.save()
            zawodnik_2.save()
        except Exception as e:
            print(e)
        super(Pojedynek, self).save(*args, **kwargs)


class Wydarzenie(models.Model):
    nazwa = models.CharField(max_length=255, null=True)
    opis = models.TextField(blank=True, null=True)
    start = models.DateTimeField(null=True)
    koniec = models.DateTimeField(null=True)

    class Meta:
        verbose_name = 'Wydarzenie'
        verbose_name_plural = 'Wydarzenia'

    def __str__(self):
        return self.nazwa
