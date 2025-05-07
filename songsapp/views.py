from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from .models import Song, Playlist

@login_required
def song_list(request):
    songs = Song.objects.all()
    return render(request, 'songs/song_list.html', {'songs': songs})

@login_required
def song_detail(request, song_id):
    song = get_object_or_404(Song, id=song_id)
    return render(request, 'songs/song_detail.html', {'song': song})

@login_required
def song_recommendations(request, song_id):
    # Get the selected song
    current_song = get_object_or_404(Song, id=song_id)
    
    # Get all songs except the current one
    all_songs = Song.objects.exclude(id=song_id)
    
    # Simple rule-based recommendation system
    recommendations = []
    
    for song in all_songs:
        # Initialize score
        score = 0
        
        # Check for matches and add points
        if song.genre == current_song.genre:
            score += 1
        if song.singer == current_song.singer:
            score += 1
        if song.music_director == current_song.music_director:
            score += 1
            
        # Only include songs with at least one match
        if score > 0:
            recommendations.append(song)
    
    # Sort recommendations by score (highest first)
    sorted_recommendations = sorted(recommendations, key=lambda x: (
        x.genre == current_song.genre,
        x.singer == current_song.singer,
        x.music_director == current_song.music_director
    ), reverse=True)
    
    return render(request, 'songs/song_recommendations.html', {
        'song': current_song,
        'recommended_songs': sorted_recommendations
    })

@login_required
@require_POST
def toggle_like(request, song_id):
    song = get_object_or_404(Song, id=song_id)
    if request.user in song.likes.all():
        song.likes.remove(request.user)
        liked = False
    else:
        song.likes.add(request.user)
        liked = True
    return JsonResponse({'liked': liked})

@login_required
@require_POST
def add_to_playlist(request, playlist_id, song_id):
    playlist = get_object_or_404(Playlist, id=playlist_id, user=request.user)
    song = get_object_or_404(Song, id=song_id)
    playlist.songs.add(song)
    return JsonResponse({'status': 'success'})

@login_required
@require_POST
def remove_from_playlist(request, playlist_id, song_id):
    playlist = get_object_or_404(Playlist, id=playlist_id, user=request.user)
    song = get_object_or_404(Song, id=song_id)
    playlist.songs.remove(song)
    return JsonResponse({'status': 'success'})

@login_required
def playlist_detail(request, playlist_id):
    playlist = get_object_or_404(Playlist, id=playlist_id, user=request.user)
    return render(request, 'songs/playlist_detail.html', {'playlist': playlist})