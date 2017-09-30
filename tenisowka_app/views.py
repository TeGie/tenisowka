from django.views.generic.list import ListView
from django.core.urlresolvers import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import *
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
import json
from django.views.generic.dates import MonthArchiveView
from django.http import Http404
from django.utils.timezone import now
from .models import *


# Index
def events(request):
    all_events = Event.objects.all()
    if request.GET:
        event_list = []
        for event in all_events:
            event_dict = {
                'title': event.name,
                'start': event.start,
                'end': event.end
            }
            event_list.append(event_dict)
        return HttpResponse(json.dumps(event_list))
    context = {
        "events": all_events
    }
    return render(request, 'tenisowka_app/index.html', context)


# Players
class Players(ListView):
    model = Player


class PlayerDetails(DetailView):
    model = Player


class AddPlayer(CreateView):
    model = Player
    fields = '__all__'
    success_url = reverse_lazy('players')


class UpdatePlayer(UpdateView):
    model = Player
    fields = '__all__'
    success_url = reverse_lazy('players')
    template_name_suffix = '_update_form'


class DeletePlayer(DeleteView):
    model = Player
    success_url = reverse_lazy('players')


# Matches
class MatchesMonthArchiveView(MonthArchiveView):
    queryset = Match.objects.all()
    date_field = 'date'
    allow_future = True
    allow_empty = True
    month_format = '%m'

    def get_month(self):
        try:
            month = super(MatchesMonthArchiveView, self).get_month()
        except Http404:
            month = now().strftime(self.get_month_format())
        return month

    def get_year(self):
        try:
            year = super(MatchesMonthArchiveView, self).get_year()
        except Http404:
            year = now().strftime(self.get_year_format())
        return year


class MatchDetails(DetailView):
    model = Match


class AddMatch(CreateView):
    model = Match
    form_class = MatchForm
    success_url = reverse_lazy('matches')


class UpdateMatch(UpdateView):
    model = Match
    template_name_suffix = '_update_form'
    form_class = MatchForm
    success_url = reverse_lazy('matches')


class DeleteMatch(DeleteView):
    model = Match
    success_url = reverse_lazy('matches')


# Events
class EventDetails(DetailView):
    model = Event


class AddEvent(CreateView):
    model = Event
    fields = '__all__'
    success_url = reverse_lazy('index')

    def get_initial(self):
        return {
            'start': self.kwargs['start'],
            'end': self.kwargs['start']
        }


class UpdateEvent(UpdateView):
    model = Event
    fields = '__all__'
    success_url = reverse_lazy('index')
    template_name_suffix = '_update_form'


class DeleteEvent(DeleteView):
    model = Event
    success_url = reverse_lazy('index')


# Attendances
class Attendances(ListView):
    model = Attendance


class AddAttendance(CreateView):
    model = Attendance
    success_url = reverse_lazy('attendances')
    form_class = AttendanceForm

    def get_form_kwargs(self, **kwargs):
        kwargs = super(AddAttendance, self).get_form_kwargs(**kwargs)
        if 'data' in kwargs:
            event = Event.objects.get(pk=self.kwargs['pk'])
            instance = Attendance(event=event)
            kwargs.update({'instance': instance})
        return kwargs
