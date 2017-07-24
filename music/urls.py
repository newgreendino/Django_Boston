from django.conf.urls import url
from . import views


app_name = "music"
# pouziva se v shortcutu misto hardcoded url v template / music:index, music:detail
urlpatterns = [
    #/music/
    url(r'^$', views.index, name="index"),

    #/music/album_id/
    url(r"^(?P<album_id>[0-9]+)/$", views.detail, name="detail"),
    # name se pouziva v template, jak nahrada za hardcoded url

    #/music/album_id/favorite
    url(r"^(?P<album_id>[0-9]+)/favorite/$", views.favorite, name="favorite"),
]