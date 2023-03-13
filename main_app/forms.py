from django import forms
from .models import Song

class SongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ['artist', 'album', 'song', 'release_year']

class SongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ['song', 'artist', 'album']