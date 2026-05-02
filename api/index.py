from flask import Flask, request, jsonify
import yt_dlp

app = Flask(__name__)

@app.route('/api/download', methods=['GET'])
def get_video_link():
    video_url = request.args.get('url')
    
    if not video_url:
        return jsonify({"success": False, "error": "Bhai, video ka URL to do!"})

    # yt-dlp ki settings YouTube bot protection bypass ke sath
    ydl_opts = {
        'format': 'best',
        'quiet': True,
        'noplaylist': True,
        'nocheckcertificate': True,
        'extractor_args': {
            'youtube': ['player_client=android', 'player_skip=webpage']
        }
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(video_url, download=False)
            
            direct_url = info_dict.get('url', None)
            title = info_dict.get('title', 'Video')

            if not direct_url:
                return jsonify({"success": False, "error": "Direct link nahi nikal saka. Shayad video private hai."})

            return jsonify({
                "success": True,
                "title": title,
                "download_url": direct_url
            })
            
    except Exception as e:
        # Ab error server crash nahi karega, balkay screen par dikhayega
        return jsonify({
            "success": False,
            "error": str(e)
        })

if __name__ == '__main__':
    app.run(debug=True)
