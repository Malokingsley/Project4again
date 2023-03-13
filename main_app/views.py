import requests
#from bs4 import BeautifulSoup
from django.shortcuts import redirect, get_object_or_404
from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from django.shortcuts import render
#from django import forms
from .models import Song
from .forms import SongForm



# Create your views here.
# Define the home view
def home(request):
  # Include an .html file extension - unlike when rendering EJS templates
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

# Add new view

def toolbox_index(request):
  # We pass data to a template very much like we did in Express!
  return render(request, 'toolboxes/index.html'
  )

def heart_radio_view(request):
    # Render the heart_radio.html template
    return render(request, 'heart_radio.html')

def get_radio_stations(request):
    stations = [
        {"name": "Hot 97 FM", "url": "https://www.iheart.com/live/hot-97-6046"},
        {"name": "SZA Radio ", "url": "https://www.iheart.com/artist/sza-30061847"},
        {"name": "WNYC's New Standards", "url": "www.iheart.com/live/wnycs-new-standards-6433"},
        # Add more stations here...
    ]
    data = {"stations": stations}
    return JsonResponse(data)


def heart_radio(request):
    stations = [
        {"name": "Hot 97 FM", "url": "https://www.iheart.com/live/hot-97-6046"},
        {"name": "SZA Radio ", "url": "https://www.iheart.com/artist/sza-30061847"},
        {"name": "WNYC's New Standards", "url": "https://www.iheart.com/live/wnycs-new-standards-6433"},
    ]
    
    if request.is_ajax() and request.method == 'GET':
        return JsonResponse({'stations': stations})
    
    return render(request, 'heart_radio.html', {'stations': stations})

def my_songs(request):
    search = request.GET.get('search', '')
    songs = Song.objects.filter(song__icontains=search)
    form = SongForm()
    return render(request, 'my_songs.html', {'songs': songs, 'search': search, 'form': form})


def add_song(request):
    if request.method == 'POST':
        form = SongForm(request.POST)
        if form.is_valid():
            song = form.save()
            return redirect('view_song', pk=song.pk)
    else:
        form = SongForm()
    return render(request, 'add_song.html', {'form': form})


def edit_song(request, pk):
    song = get_object_or_404(Song, pk=pk)
    if request.method == 'POST':
        form = SongForm(request.POST, instance=song)
        if form.is_valid():
            form.save()
            return redirect('my_song')
    else:
        form = SongForm(instance=song)
    return render(request, 'edit_song.html', {'form': form})


def delete_song(request, pk):
    song = Song.objects.get(pk=pk)
    song.delete()
    return redirect('my_songs')


def view_song(request, pk):
    song = Song.objects.get(pk=pk)
    return render(request, 'view_song.html', {'song': song})
