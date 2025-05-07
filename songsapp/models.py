from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

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
    
    def __str__(self):
        return self.title
        
    class Meta:
        ordering = ['-rating', 'title']