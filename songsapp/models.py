from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User

class Song(models.Model):
    title = models.CharField(max_length=200)
    genre = models.CharField(max_length=100)
    singer = models.CharField(max_length=200)
    music_director = models.CharField(max_length=200)
    movie_name = models.CharField(max_length=200, blank=True, null=True)
    image = models.ImageField(upload_to='songs/images/', default='songs/images/default.jpg')
    audio_file = models.FileField(upload_to='songs/audio/', null=True, blank=True)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='liked_songs', blank=True)
    
    def __str__(self):
        return self.title
        
    class Meta:
        ordering = ['-rating', 'title']

class Playlist(models.Model):
    name = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='playlists')
    songs = models.ManyToManyField(Song, related_name='playlists')
    created_at = models.DateTimeField(auto_now_add=True)
    is_public = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.user.username}'s {self.name}"
    
    class Meta:
        ordering = ['-created_at']