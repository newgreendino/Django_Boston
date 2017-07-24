from django.db import models

# Create your models here.


class Album(models.Model):
    name = models.CharField(max_length=100)
    no_songs = models.PositiveSmallIntegerField
    artist = models.CharField(max_length=100)
    likes_on_facebook = models.IntegerField

    def __str__(self):
        return self.name + " - " + self.artist


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    file_type = models.CharField(max_length=10)
    is_favourite = models.BooleanField(default=False)

    def __str__(self):
        return self.title