from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Song

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
            recommendations.append({
                'song': song,
                'score': score,
                'matches': []
            })
            
            # Add match details for display
            if song.genre == current_song.genre:
                recommendations[-1]['matches'].append('Genre')
            if song.singer == current_song.singer:
                recommendations[-1]['matches'].append('Singer')
            if song.music_director == current_song.music_director:
                recommendations[-1]['matches'].append('Music Director')
    
    # Sort recommendations by score (highest first)
    sorted_recommendations = sorted(recommendations, key=lambda x: x['score'], reverse=True)
    
    return render(request, 'songs/recommendations.html', {
        'current_song': current_song,
        'recommendations': sorted_recommendations
    })