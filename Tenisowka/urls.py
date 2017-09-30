"""Tenisowka URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from tenisowka_app.views import *
from django.contrib.auth import views as auth_views
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm

urlpatterns = [
    # admin, login, register, etc
    url(r'^admin/', admin.site.urls),

    url('^register/', CreateView.as_view(
            template_name ='registration/register.html',
            form_class = UserCreationForm,
            success_url = '/login/'
        ), name='register'),

    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'login'}, name='logout'),

    url(r'^password_reset/$', auth_views.password_reset,
        {'template_name':'registration/password_reset.html'},
        name='password_reset'),
    url(r'^password_reset/done/$', auth_views.password_reset_done,
        {'template_name':'registration/password_done.html'},
        name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.password_reset_confirm, {'template_name':'registration/password_confirm.html'},
        name='password_reset_confirm'),
    url(r'^reset/done/$', auth_views.password_reset_complete,
        {'template_name':'registration/password_complete.html'},
        name='password_reset_complete'),

    # site nav
    url(r'^index/$', events, name='index'),
    url(r'^wydarzenie/(?P<pk>[0-9]+)/$', EventDetails.as_view(), name='event'),
    url(r'^wydarzenie/dodaj/(?P<date>(0[1-9]|1[0-2])\/(0[1-9]|1\d|2\d|3[01])\/(19|20)\d{2})/$',
        AddEvent.as_view(),
        name='add_event'),
    url(r'^wydarzenie/(?P<pk>[0-9]+)/aktualizuj/$', UpdateEvent.as_view(), name='update_event'),
    url(r'^wydarzenie/(?P<pk>[0-9]+)/usun/$', DeleteEvent.as_view(), name='delete_event'),

    url(r'^zawodnicy/$', Players.as_view(), name='players'),
    url(r'^zawodnik/(?P<pk>[0-9]+)/$', PlayerDetails.as_view(), name='player'),
    url(r'^zawodnik/dodaj/$', AddPlayer.as_view(), name='add_player'),
    url(r'^zawodnik/(?P<pk>[0-9]+)/aktualizuj/$', UpdatePlayer.as_view(), name='update_player'),
    url(r'^zawodnik/(?P<pk>[0-9]+)/usun/$', DeletePlayer.as_view(), name='delete_player'),

    url(r'^pojedynki/$', MatchesMonthArchiveView.as_view(), name='matches'),
    url(r'^pojedynki/(?P<year>[0-9]{4})/(?P<month>[0-9]+)/$',
        MatchesMonthArchiveView.as_view(),
        name="matches"),
    url(r'^pojedynek/(?P<pk>[0-9]+)/$', MatchDetails.as_view(), name='match'),
    url(r'^pojedynek/dodaj/$', AddMatch.as_view(), name='add_match'),
    url(r'^pojedynek/(?P<pk>[0-9]+)/aktualizuj/$', UpdateMatch.as_view(), name='update_match'),

    url(r'^obecnosci/$', Attendances.as_view(), name='attendances'),
    url(r'^obecnosci/(?P<pk>[0-9]+)/dodaj/$', AddAttendance.as_view(), name='add_attendance')
]