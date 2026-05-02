from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/api/download', methods=['GET'])
def get_video_link():
    video_url = request.args.get('url')
    
    if not video_url:
        return jsonify({"success": False, "error": "Bhai, video ka URL to do!"})

    # Cobalt API - Yeh third-party server hai jo bot protection aur timeouts handle karta hai
    api_url = "https://api.cobalt.tools/api/json"
    
    # Servers ko dhoka dene ke liye original headers
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Origin": "https://cobalt.tools",
        "Referer": "https://cobalt.tools/",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    
    # API ko payload bhejna (720p quality aur classic file name)
    payload = {
        "url": video_url,
        "vQuality": "720", 
        "filenamePattern": "classic"
    }

    try:
        # API ko request bhejna (is mein sirf 1-2 seconds lagte hain)
        response = requests.post(api_url, headers=headers, json=payload)
        data = response.json()

        # Agar API ne successfully link nikal liya (redirect, stream, ya picker mode)
        if data.get("status") in ["redirect", "stream", "success", "picker"]:
            direct_link = data.get("url")
            
            # Agar API multiple links de (jaise alag se video/audio), to pehla utha lo
            if data.get("status") == "picker":
                direct_link = data["picker"][0]["url"]

            return jsonify({
                "success": True,
                "title": "Video Ready (Bot Bypassed!)", 
                "download_url": direct_link
            })
        else:
            return jsonify({
                "success": False,
                "error": data.get("text", "API video nikalne mein fail ho gayi. Shayad link private hai.")
            })
            
    except Exception as e:
        return jsonify({
            "success": False,
            "error": f"Connection Error: {str(e)}"
        })

if __name__ == '__main__':
    app.run(debug=True)
