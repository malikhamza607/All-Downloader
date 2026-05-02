from flask import Flask, request, jsonify
import yt_dlp

app = Flask(__name__)

@app.route('/api/download', methods=['GET'])
def get_video_link():
    # User se URL lena
    video_url = request.args.get('url')
    
    if not video_url:
        return jsonify({"error": "Bhai, video ka URL to do!"}), 400

    # yt-dlp ki settings (sirf link nikalna hai, download nahi karna)
    ydl_opts = {
        'format': 'best',
        'quiet': True,
        'noplaylist': True
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # Info extract karna (download=False zaroori hai Vercel ke liye)
            info_dict = ydl.extract_info(video_url, download=False)
            
            # Direct video ka link aur title nikalna
            direct_url = info_dict.get('url', None)
            title = info_dict.get('title', 'Video')

            return jsonify({
                "success": True,
                "title": title,
                "download_url": direct_url
            })
            
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

# Vercel ko app run karne ke liye iski zaroorat hoti hai
if __name__ == '__main__':
    app.run(debug=True)
