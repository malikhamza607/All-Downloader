from http.server import BaseHTTPRequestHandler
import json
import yt_dlp
import urllib.parse
import os
import tempfile

def get_video_info(url: str) -> dict:
“”“Extract video info without downloading”””
ydl_opts = {
“quiet”: True,
“no_warnings”: True,
“extract_flat”: False,
“skip_download”: True,
}

```
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    info = ydl.extract_info(url, download=False)
    
    formats = []
    if info.get("formats"):
        seen = set()
        for f in info["formats"]:
            quality = f.get("format_note") or f.get("height") or ""
            ext = f.get("ext", "")
            fid = f.get("format_id", "")
            
            # Only include video formats with both video+audio or audio-only
            has_video = f.get("vcodec") and f.get("vcodec") != "none"
            has_audio = f.get("acodec") and f.get("acodec") != "none"
            
            if (has_video and has_audio) or (not has_video and has_audio):
                label = f"{quality} .{ext}" if quality else f".{ext}"
                key = f"{quality}-{ext}"
                if key not in seen and ext in ["mp4", "webm", "m4a", "mp3"]:
                    seen.add(key)
                    filesize = f.get("filesize") or f.get("filesize_approx")
                    formats.append({
                        "format_id": fid,
                        "label": label,
                        "ext": ext,
                        "quality": str(quality),
                        "filesize": filesize,
                        "url": f.get("url", ""),
                    })
    
    # Sort by quality (higher = better)
    def sort_key(f):
        q = f.get("quality", "")
        try:
            return -int(str(q).replace("p", ""))
        except:
            return 0
    
    formats.sort(key=sort_key)
    
    return {
        "title": info.get("title", "Unknown"),
        "thumbnail": info.get("thumbnail", ""),
        "duration": info.get("duration", 0),
        "uploader": info.get("uploader", ""),
        "platform": detect_platform(url),
        "formats": formats[:8],  # Limit to 8 formats
        "direct_url": info.get("url", ""),
    }
```

def detect_platform(url: str) -> str:
url_lower = url.lower()
if “youtube.com” in url_lower or “youtu.be” in url_lower:
return “YouTube”
elif “instagram.com” in url_lower:
return “Instagram”
elif “tiktok.com” in url_lower:
return “TikTok”
elif “twitter.com” in url_lower or “x.com” in url_lower:
return “Twitter/X”
elif “facebook.com” in url_lower or “fb.watch” in url_lower:
return “Facebook”
else:
return “Video”

class handler(BaseHTTPRequestHandler):

```
def do_OPTIONS(self):
    self.send_response(200)
    self._set_cors_headers()
    self.end_headers()

def do_GET(self):
    parsed = urllib.parse.urlparse(self.path)
    params = urllib.parse.parse_qs(parsed.query)
    
    if parsed.path == "/api/download":
        video_url = params.get("url", [None])[0]
        
        if not video_url:
            self._json_response({"error": "URL parameter required"}, 400)
            return
        
        try:
            info = get_video_info(video_url)
            self._json_response({"success": True, "data": info})
        except yt_dlp.utils.DownloadError as e:
            error_msg = str(e)
            if "Private" in error_msg or "private" in error_msg:
                msg = "This video is private."
            elif "removed" in error_msg or "deleted" in error_msg:
                msg = "This video has been removed."
            elif "age" in error_msg.lower():
                msg = "Age-restricted video."
            else:
                msg = "Could not fetch video. Check the URL and try again."
            self._json_response({"error": msg}, 422)
        except Exception as e:
            self._json_response({"error": f"Unexpected error: {str(e)}"}, 500)
    else:
        self._json_response({"error": "Not found"}, 404)

def _set_cors_headers(self):
    self.send_header("Access-Control-Allow-Origin", "*")
    self.send_header("Access-Control-Allow-Methods", "GET, OPTIONS")
    self.send_header("Access-Control-Allow-Headers", "Content-Type")

def _json_response(self, data: dict, status: int = 200):
    body = json.dumps(data).encode("utf-8")
    self.send_response(status)
    self._set_cors_headers()
    self.send_header("Content-Type", "application/json")
    self.send_header("Content-Length", str(len(body)))
    self.end_headers()
    self.wfile.write(body)

def log_message(self, format, *args):
    pass  # Suppress default logging
```