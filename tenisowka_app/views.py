from django.views.generic.list import ListView
from django.core.urlresolvers import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from tenisowka_app.forms import *
from django.shortcuts import render, redirect
from django.http import HttpResponse
import json
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic.dates import MonthArchiveView
from django.http import Http404
from django.utils.timezone import now


########## Index #########
def wydarzenia(request):
    all_events = Wydarzenie.objects.all()
    if request.GET:
        event_arr = []
        for i in all_events:
            event_sub_dict = {
                'title': i.nazwa,
                'start': i.start,
                'end': i.koniec
            }
            event_arr.append(event_sub_dict)
        return HttpResponse(json.dumps(event_arr))
    context = {
        "events": all_events
    }
    return render(request, 'tenisowka_app/glowna.html', context)


########## Zawodnicy #########
class Zawodnicy(ListView):
    model = Zawodnik


class ZobaczZawodnika(DetailView):
    model = Zawodnik


class DodajZawodnika(CreateView):
    model = Zawodnik
    fields = '__all__'
    success_url = reverse_lazy('zawodnicy')


class AktualizujZawodnika( UpdateView):
    model = Zawodnik
    fields = '__all__'
    success_url = reverse_lazy('zawodnicy')
    template_name_suffix = '_update_form'


class UsunZawodnika(DeleteView):
    model = Zawodnik
    success_url = reverse_lazy('zawodnicy')


########## Pojedynki #########
class PojedynkiMonthArchiveView(MonthArchiveView):
    queryset = Pojedynek.objects.all()
    date_field = 'data'
    allow_future = True
    month_format = '%m'
    year_format = '%Y'

    def get_month(self):
        try:
            month = super(PojedynkiMonthArchiveView, self).get_month()
        except Http404:
            month = now().strftime(self.get_month_format())
        return month

    def get_year(self):
        try:
            year = super(PojedynkiMonthArchiveView, self).get_year()
        except Http404:
            year = now().strftime(self.get_year_format())
        return year


class ZobaczPojedynek(DetailView):
    model = Pojedynek


class DodajPojedynek(CreateView):
    model = Pojedynek
    success_url = reverse_lazy('pojedynki')
    form_class = DodajPojedynekForm


class AktualizujPojedynek(UpdateView):
    model = Wydarzenie
    fields = '__all__'
    success_url = reverse_lazy('pojedynki')
    template_name_suffix = '_update_form'


class UsunPojedynek(DeleteView):
    model = Wydarzenie
    success_url = reverse_lazy('pojedynki')


########## Wydarzenia #########
class ZobaczWydarzenie( DetailView):
    model = Wydarzenie


class DodajWydarzenie(CreateView):
    model = Wydarzenie
    fields = '__all__'
    success_url = reverse_lazy('index')

    def get_initial(self):
        return {
            'start': self.kwargs['start'],
            'koniec': self.kwargs['start']
        }


class AktualizujWydarzenie(UpdateView):
    model = Wydarzenie
    fields = '__all__'
    success_url = reverse_lazy('index')
    template_name_suffix = '_update_form'


class UsunWydarzenie(DeleteView):
    model = Wydarzenie
    success_url = reverse_lazy('index')
