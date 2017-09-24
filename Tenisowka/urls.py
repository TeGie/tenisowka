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

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'login' }, name='logout'),
    url(r'^zawodnicy/$', Zawodnicy.as_view(), name='zawodnicy'),
    url(r'^zawodnik/(?P<pk>[0-9]+)/$', ZobaczZawodnika.as_view(), name='zawodnik'),
    url(r'^zawodnik/dodaj/$', DodajZawodnika.as_view(),name='dodaj_zawodnika'),
    url(r'^zawodnik/(?P<pk>[0-9]+)/aktualizuj/$', AktualizujZawodnika.as_view(),name='aktualizuj_zawodnika'),
    url(r'^zawodnik/(?P<pk>[0-9]+)/usun/$', UsunZawodnika.as_view(),name='usun_zawodnika'),
    url(r'^pojedynek/dodaj/$', DodajPojedynek.as_view(),name='dodaj_pojedynek'),
    url(r'^pojedynki/$', Pojedynki.as_view(), name='pojedynki'),
    url(r'^pojedynek/(?P<pk>[0-9]+)/$', ZobaczPojedynek.as_view()),
    url(r'^index/$', wydarzenia, name='index'),
    url(r'^wydarzenie/dodaj/$', DodajWydarzenie.as_view(), name='dodaj_wydarzenie'),
    url(r'^wydarzenie/(?P<pk>[0-9]+)/aktualizuj/$', AktualizujWydarzenie.as_view(), name='aktualizuj_wydarzenie'),
    url(r'^wydarzenie/(?P<pk>[0-9]+)/usun/$', UsunWydarzenie.as_view(), name='usun_wydarzenie'),
    url(r'^wydarzenie/(?P<pk>[0-9]+)/$', ZobaczWydarzenie.as_view(), name='zobacz_wydarzenie')
]