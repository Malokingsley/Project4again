from django.db import models
from django.contrib.auth.models import User
from django import forms
# Create your models here.

class Song(models.Model):
    artist = models.CharField(max_length=40)
    album = models.CharField(max_length=40)
    song = models.CharField(max_length=40)
    release_year = models.PositiveIntegerField(null=True, blank=True)
    #user = models.ForeignKey(User, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.song

class RadioStation(models.Model):
    name = models.CharField(max_length=40)
    url = models.URLField()

    def __str__(self):
        return self.name
    

class FavoriteSong(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favoritesongs')
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'song')

    def __str__(self):
        return str(self.song)

    

