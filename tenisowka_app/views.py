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


########## Index #########
@login_required(login_url='/login/')
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
class Zawodnicy(LoginRequiredMixin, ListView):
    model = Zawodnik
    login_url = '/login/'


class ZobaczZawodnika(LoginRequiredMixin, DetailView):
    model = Zawodnik
    login_url = '/login/'


class DodajZawodnika(LoginRequiredMixin, CreateView):
    model = Zawodnik
    fields = '__all__'
    success_url = reverse_lazy('zawodnicy')
    login_url = '/login/'


class AktualizujZawodnika(LoginRequiredMixin, UpdateView):
    model = Zawodnik
    fields = '__all__'
    success_url = reverse_lazy('zawodnicy')
    template_name_suffix = '_update_form'
    login_url = '/login/'


class UsunZawodnika(LoginRequiredMixin, DeleteView):
    model = Zawodnik
    success_url = reverse_lazy('zawodnicy')
    login_url = '/login/'

########## Pojedynki #########
class Pojedynki(LoginRequiredMixin, ListView):
    model = Pojedynek
    login_url = '/login/'


class ZobaczPojedynek(LoginRequiredMixin, DetailView):
    model = Pojedynek
    login_url = '/login/'


class DodajPojedynek(LoginRequiredMixin, CreateView):
    model = Pojedynek
    success_url = reverse_lazy('pojedynki')
    form_class = DodajPojedynekForm
    login_url = '/login/'


class AktualizujPojedynek(LoginRequiredMixin, UpdateView):
    model = Wydarzenie
    fields = '__all__'
    success_url = reverse_lazy('pojedynki')
    template_name_suffix = '_update_form'
    login_url = '/login/'


class UsunPojedynek(LoginRequiredMixin, DeleteView):
    model = Wydarzenie
    success_url = reverse_lazy('pojedynki')
    login_url = '/login/'


########## Wydarzenia #########
class ZobaczWydarzenie(LoginRequiredMixin, DetailView):
    model = Wydarzenie
    login_url = '/login/'


class DodajWydarzenie(LoginRequiredMixin, CreateView):
    model = Wydarzenie
    fields = '__all__'
    success_url = reverse_lazy('index')
    login_url = '/login/'

    def get_initial(self):
        return {
            'start': self.kwargs['start'],
            'koniec': self.kwargs['start']
        }


class AktualizujWydarzenie(LoginRequiredMixin, UpdateView):
    model = Wydarzenie
    fields = '__all__'
    success_url = reverse_lazy('index')
    template_name_suffix = '_update_form'
    login_url = '/login/'


class UsunWydarzenie(LoginRequiredMixin, DeleteView):
    model = Wydarzenie
    success_url = reverse_lazy('index')
    login_url = '/login/'
