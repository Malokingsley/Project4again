from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    # route for my songs
    path('my_songs/', views.my_songs, name='my_songs'),
    # add song CRUD
    path('add_song/', views.add_song, name='add_song'),
    path('song/<int:pk>/', views.view_song, name='view_song'),
    path('song/<int:pk>/edit/', views.edit_song, name='edit_song'),
    path('song/<int:pk>/delete/', views.delete_song, name='delete_song'),

    

    # route for iheart radio
    path('heart_radio/', views.heart_radio_view, name='heart_radio'),
    path('get_radio_stations/', views.get_radio_stations, name='get_radio_stations'),
   

]

    