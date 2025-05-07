from django.urls import path
from . import views

app_name = 'songsapp'

urlpatterns = [
    path('', views.song_list, name='song_list'),
    path('<int:song_id>/', views.song_detail, name='song_detail'),
    path('<int:song_id>/recommendations/', views.song_recommendations, name='song_recommendations'),
]