from django.contrib import admin
from .models import Song

@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre', 'singer', 'music_director', 'movie_name', 'rating')
    list_filter = ('genre', 'singer', 'music_director', 'rating')
    search_fields = ('title', 'movie_name', 'singer', 'music_director')
    ordering = ('-rating', 'title')