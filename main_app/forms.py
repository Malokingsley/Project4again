from django import forms
from .models import Song, FavoriteSong



class SongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ['artist', 'album', 'song', 'release_year']

class FavoriteSongForm(forms.ModelForm):
    class Meta:
        model = FavoriteSong
        fields = ['song']