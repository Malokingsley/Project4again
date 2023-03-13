from django.db import models

# Create your models here.

class Song(models.Model):
    artist = models.CharField(max_length=40)
    album = models.CharField(max_length=40)
    song = models.CharField(max_length=40)
    release_year = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return self.song
