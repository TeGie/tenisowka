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
    # admin, login, register, etc
    url(r'^admin/', admin.site.urls),
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
    url(r'^index/$', wydarzenia, name='index'),
    url(r'^zawodnicy/$', Zawodnicy.as_view(), name='zawodnicy'),
    url(r'^zawodnik/(?P<pk>[0-9]+)/$', ZobaczZawodnika.as_view(), name='zawodnik'),
    url(r'^zawodnik/dodaj/$', DodajZawodnika.as_view(),name='dodaj_zawodnika'),
    url(r'^zawodnik/(?P<pk>[0-9]+)/aktualizuj/$', AktualizujZawodnika.as_view(),name='aktualizuj_zawodnika'),
    url(r'^zawodnik/(?P<pk>[0-9]+)/usun/$', UsunZawodnika.as_view(),name='usun_zawodnika'),
    url(r'^pojedynek/dodaj/$', DodajPojedynek.as_view(),name='dodaj_pojedynek'),
    url(r'^pojedynki/$', Pojedynki.as_view(), name='pojedynki'),
    url(r'^pojedynek/(?P<pk>[0-9]+)/$', ZobaczPojedynek.as_view()),
    url(r'^wydarzenie/dodaj/(?P<start>((0|1)\d{1})/((0|1|2)\d{1})/((19|20)\d{2}))/$',
        DodajWydarzenie.as_view(),
        name='dodaj_wydarzenie'),
    url(r'^wydarzenie/(?P<pk>[0-9]+)/aktualizuj/$', AktualizujWydarzenie.as_view(), name='aktualizuj_wydarzenie'),
    url(r'^wydarzenie/(?P<pk>[0-9]+)/usun/$', UsunWydarzenie.as_view(), name='usun_wydarzenie'),
    url(r'^wydarzenie/(?P<pk>[0-9]+)/$', ZobaczWydarzenie.as_view(), name='zobacz_wydarzenie')
]