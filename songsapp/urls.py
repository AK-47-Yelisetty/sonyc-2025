from django.urls import path
from . import views

app_name = 'songsapp'

urlpatterns = [
    path('', views.song_list, name='song_list'),
    path('<int:song_id>/', views.song_detail, name='song_detail'),
    path('<int:song_id>/recommendations/', views.song_recommendations, name='song_recommendations'),
    path('<int:song_id>/toggle-like/', views.toggle_like, name='toggle_like'),
    path('playlists/<int:playlist_id>/', views.playlist_detail, name='playlist_detail'),
    path('playlists/<int:playlist_id>/add-song/<int:song_id>/', views.add_to_playlist, name='add_to_playlist'),
    path('playlists/<int:playlist_id>/remove-song/<int:song_id>/', views.remove_from_playlist, name='remove_from_playlist'),
]