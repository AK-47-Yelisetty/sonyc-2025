import os
import django
import shutil
from pathlib import Path

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'musicproject.settings')
django.setup()

from django.contrib.auth.models import User
from songsapp.models import Song

def create_superuser():
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser('admin', 'admin@example.com', 'admin')
        print('Superuser created: admin/admin')
    else:
        print('Superuser already exists')

def create_sample_songs():
    # Create sample songs
    sample_songs = [
        {
            'title': 'Shape of You',
            'genre': 'Pop',
            'singer': 'Ed Sheeran',
            'music_director': 'Ed Sheeran',
            'movie_name': None,
            'rating': 5,
        },
        {
            'title': 'Blinding Lights',
            'genre': 'Synth-pop',
            'singer': 'The Weeknd',
            'music_director': 'The Weeknd',
            'movie_name': None,
            'rating': 5,
        },
        {
            'title': 'Dance Monkey',
            'genre': 'Pop',
            'singer': 'Tones and I',
            'music_director': 'Tones and I',
            'movie_name': None,
            'rating': 4,
        },
        {
            'title': 'Levitating',
            'genre': 'Pop',
            'singer': 'Dua Lipa',
            'music_director': 'Dua Lipa',
            'movie_name': None,
            'rating': 4,
        },
        {
            'title': 'Save Your Tears',
            'genre': 'Synth-pop',
            'singer': 'The Weeknd',
            'music_director': 'The Weeknd',
            'movie_name': None,
            'rating': 4,
        },
        {
            'title': 'Perfect',
            'genre': 'Pop',
            'singer': 'Ed Sheeran',
            'music_director': 'Ed Sheeran',
            'movie_name': None,
            'rating': 5,
        },
        {
            'title': 'Believer',
            'genre': 'Rock',
            'singer': 'Imagine Dragons',
            'music_director': 'Imagine Dragons',
            'movie_name': None,
            'rating': 5,
        },
        {
            'title': 'Thunder',
            'genre': 'Rock',
            'singer': 'Imagine Dragons',
            'music_director': 'Imagine Dragons',
            'movie_name': None,
            'rating': 4,
        },
        {
            'title': 'Despacito',
            'genre': 'Reggaeton',
            'singer': 'Luis Fonsi',
            'music_director': 'Daddy Yankee',
            'movie_name': None,
            'rating': 5,
        },
        {
            'title': 'My Heart Will Go On',
            'genre': 'Pop',
            'singer': 'Celine Dion',
            'music_director': 'James Horner',
            'movie_name': 'Titanic',
            'rating': 5,
        },
    ]

    # Check if we already have songs
    if Song.objects.count() == 0:
        print('Creating sample songs...')
        for song_data in sample_songs:
            Song.objects.create(**song_data)
        print(f'Created {len(sample_songs)} sample songs')
    else:
        print('Songs already exist in the database')

def setup_default_image():
    # Make sure the default image is copied to the media directory
    media_root = Path('media/songs/images')
    media_root.mkdir(parents=True, exist_ok=True)
    
    static_image = Path('songs/static/songs/images/default.svg')
    if static_image.exists():
        # Copy the static SVG to the media folder and rename to .jpg (for simplicity)
        media_path = media_root / 'default.jpg'
        if not media_path.exists():
            print('Setting up default image...')
            shutil.copy(static_image, media_path)
            print('Default image copied to media folder')
        else:
            print('Default image already exists')

if __name__ == '__main__':
    print('Setting up sample data...')
    create_superuser()
    setup_default_image()
    create_sample_songs()
    print('Done!')