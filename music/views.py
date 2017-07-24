# from django.http import HttpResponse / pro return HttpResponse
from django.http import Http404

# from django.template import loader / neni potreba kdyz delam shortcut
from django.shortcuts import render, get_object_or_404
from .models import Album, Song

# bez template!!!!

# def index(request):
#     all_albums = Album.objects.all()
#     html = ""
#
#     for album in all_albums:
#         url = "/music/" + str(album.id) + "/"
#         html += "<a href='" + url + "'>" + album.name + "</a><br>"
#
#     return HttpResponse(html)


# clasicky template !!!!

# def index(request):
#     all_albums = Album.objects.all()
#     template = loader.get_template("music/index.html")
#     context = {
#         "all_albums":all_albums
#     }
#     return HttpResponse(template.render(context,request))

# template shortcut !!!!

def index(request):
    all_albums = Album.objects.all()
    context = {"all_albums":all_albums}
    return render(request, "music/index.html", context)


def detail(request, album_id):
    # bez shortcutu get_object_or_404
    # try:
    #     album = Album.objects.get(id=album_id)
    #
    # except Album.DoesNotExist:
    #     raise Http404("Album neexistuje")
    #
    # se shortcutem - get_object_or_404

    album = get_object_or_404(Album, id=album_id)
    return render(request, "music/detail.html", {'album': album})


def favorite(request, album_id):
    album = get_object_or_404(Album, id=album_id)
    try:
        selected_song = album.song_set.get(id=request.POST["song"])
    except (KeyError, Song.DoesNotExist):
        return (request, "music/detail.html", {
            'album': album,
            'error_message': "Select any song",
        })
    else:
        if selected_song.is_favourite:
            selected_song.is_favourite = False
        else:
            selected_song.is_favourite = True
        selected_song.save()
        return render(request, "music/detail.html", {'album': album})