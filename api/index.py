from flask import Flask, request, jsonify
import yt_dlp
import os

app = Flask(__name__)

@app.route('/api/download', methods=['GET'])
def get_video_link():
    video_url = request.args.get('url')
    
    if not video_url:
        return jsonify({"success": False, "error": "Bhai, video ka URL to do!"})

    # Cookies file ko api folder ke andar dhoondna
    cookie_path = os.path.join(os.path.dirname(__file__), 'cookies.txt')

    # yt-dlp ki nayi aur safe settings (Real Browser trick)
    ydl_opts = {
        'format': 'best',
        'quiet': True,
        'noplaylist': True,
        'nocheckcertificate': True,
        'cookiefile': cookie_path, # Cookies attach kar di
        'http_headers': {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        }
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # Info nikalna
            info_dict = ydl.extract_info(video_url, download=False)
            
            direct_url = info_dict.get('url', None)
            title = info_dict.get('title', 'Video')

            if not direct_url:
                return jsonify({"success": False, "error": "Direct link nahi mila. Shayad video private hai."})

            return jsonify({
                "success": True,
                "title": title,
                "download_url": direct_url
            })
            
    except Exception as e:
        return jsonify({
            "success": False,
            "error": f"Connection Error: {str(e)}"
        })

if __name__ == '__main__':
    app.run(debug=True)
