    # yt-dlp ki settings
    ydl_opts = {
        'format': 'best',
        'quiet': True,
        'noplaylist': True,
        'extractor_args': {
            'youtube': ['player_client=android', 'player_skip=webpage']
        }
    }
