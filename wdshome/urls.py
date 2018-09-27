from django.conf.urls import url
from . import views

app_name = 'wdshome'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register$', views.register, name='register'),
    url(r'^login_user$', views.login_user, name='login_user'),
    url(r'^logout_user$', views.logout_user, name='logout_user'),
    url(r'^ny_annonse$', views.ny_annonse, name='ny_annonse'),
    url(r'^annonser$', views.annonser, name='annonser'),
    url(r'^annonse+(?P<annonser_id>[0-9]+)/$', views.spesifikk_annonse, name='spesifikk_annonse'),
    url(r'^mine_annonser$', views.mine_annonser, name='mine_annonser'),
    url(r'^min_profil$', views.min_profil, name='min_profil'),
    url(r'^rediger_profil$', views.rediger_profil, name='rediger_profil'),
    url(r'^ny_utvikler$', views.ny_utvikler, name='ny_utvikler'),
    url(r'^utviklere$', views.utviklere, name='utviklere'),
    url(r'^utvikler+(?P<utviklere_id>[0-9]+)/$', views.spesifikk_utviklere, name='spesifikk_utviklere'),
    url(r'^slett_annonse+(?P<annonser_id>[0-9]+)/$', views.slett_annonse, name='slett_annonse'),
    url(r'^soknad+(?P<annonser_id>[0-9]+)/$', views.søknad, name='søknad'),
    url(r'^soknader+(?P<søknader_id>[0-9]+)/$', views.søknader, name='søknader'),
    url(r'^mine_søknader$', views.mine_søknader, name='mine_søknader'),
]