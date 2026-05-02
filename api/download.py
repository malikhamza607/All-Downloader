from http.server import BaseHTTPRequestHandler
import json
import urllib.parse
import urllib.request
import re

# ─────────────────────────────────────────────

# Platform detector

# ─────────────────────────────────────────────

def detect_platform(url: str) -> str:
u = url.lower()
if “youtube.com” in u or “youtu.be” in u:
return “youtube”
if “instagram.com” in u:
return “instagram”
if “tiktok.com” in u:
return “tiktok”
if “twitter.com” in u or “x.com” in u:
return “twitter”
if “facebook.com” in u or “fb.watch” in u:
return “facebook”
return “other”

# ─────────────────────────────────────────────

# YouTube video ID extractor

# ─────────────────────────────────────────────

def get_yt_id(url: str):
patterns = [
r”(?:youtube.com/watch?v=|youtu.be/|youtube.com/embed/|youtube.com/shorts/)([^&\n?#]{11})”
]
for p in patterns:
m = re.search(p, url)
if m:
return m.group(1)
return None

# ─────────────────────────────────────────────

# noembed metadata (no API key)

# ─────────────────────────────────────────────

def get_noembed(url: str) -> dict:
try:
api = f”https://noembed.com/embed?url={urllib.parse.quote(url)}”
req = urllib.request.Request(api, headers={“User-Agent”: “Mozilla/5.0”})
with urllib.request.urlopen(req, timeout=8) as r:
return json.loads(r.read())
except Exception:
return {}

# ─────────────────────────────────────────────

# YouTube handler

# ─────────────────────────────────────────────

def handle_youtube(url: str) -> dict:
vid = get_yt_id(url)
if not vid:
raise ValueError(“Valid YouTube URL nahi hai.”)

```
meta = get_noembed(url)
title = meta.get("title", "YouTube Video")
author = meta.get("author_name", "")
thumb = meta.get("thumbnail_url") or f"https://img.youtube.com/vi/{vid}/hqdefault.jpg"

encoded = urllib.parse.quote(url, safe="")
vid_enc = urllib.parse.quote(vid, safe="")

formats = [
    {
        "quality": "COBALT",
        "label": "Best Quality · No Watermark",
        "url": f"https://cobalt.tools/?u={encoded}",
        "type": "web",
        "recommended": True,
    },
    {
        "quality": "Y2MATE",
        "label": "HD · SD · MP3",
        "url": f"https://www.y2mate.com/youtube/{vid_enc}",
        "type": "web",
    },
    {
        "quality": "SAVEFROM",
        "label": "Multiple Formats",
        "url": f"https://en.savefrom.net/#url={encoded}",
        "type": "web",
    },
    {
        "quality": "SSTUBE",
        "label": "Fast Download",
        "url": f"https://www.sstube.online/watch?v={vid_enc}",
        "type": "web",
    },
    {
        "quality": "MP3 ONLY",
        "label": "Audio Download",
        "url": f"https://www.y2mate.com/youtube-mp3/{vid_enc}",
        "type": "web",
    },
]

return {
    "platform": "YouTube",
    "title": title,
    "author": author,
    "thumbnail": thumb,
    "formats": formats,
}
```

# ─────────────────────────────────────────────

# Instagram handler

# ─────────────────────────────────────────────

def handle_instagram(url: str) -> dict:
encoded = urllib.parse.quote(url, safe=””)
formats = [
{
“quality”: “SNAPINSTA”,
“label”: “Reels · Posts · Stories”,
“url”: f”https://snapinsta.app/?url={encoded}”,
“type”: “web”,
“recommended”: True,
},
{
“quality”: “IGDL”,
“label”: “HD Video Download”,
“url”: f”https://igdownloader.app/?url={encoded}”,
“type”: “web”,
},
{
“quality”: “FASTDL”,
“label”: “Quick & Easy”,
“url”: f”https://fastdl.app/instagram?url={encoded}”,
“type”: “web”,
},
{
“quality”: “COBALT”,
“label”: “Universal Downloader”,
“url”: f”https://cobalt.tools/?u={encoded}”,
“type”: “web”,
},
]
return {
“platform”: “Instagram”,
“title”: “Instagram Video”,
“author”: “”,
“thumbnail”: “”,
“formats”: formats,
}

# ─────────────────────────────────────────────

# TikTok handler

# ─────────────────────────────────────────────

def handle_tiktok(url: str) -> dict:
encoded = urllib.parse.quote(url, safe=””)
formats = [
{
“quality”: “SSSTIK”,
“label”: “No Watermark · HD”,
“url”: f”https://ssstik.io/en?url={encoded}”,
“type”: “web”,
“recommended”: True,
},
{
“quality”: “SNAPTIK”,
“label”: “Fast TikTok DL”,
“url”: f”https://snaptik.app/?url={encoded}”,
“type”: “web”,
},
{
“quality”: “TIKMATE”,
“label”: “Free & Easy”,
“url”: f”https://tikmate.online/?url={encoded}”,
“type”: “web”,
},
{
“quality”: “COBALT”,
“label”: “Best Quality”,
“url”: f”https://cobalt.tools/?u={encoded}”,
“type”: “web”,
},
]
return {
“platform”: “TikTok”,
“title”: “TikTok Video”,
“author”: “”,
“thumbnail”: “”,
“formats”: formats,
}

# ─────────────────────────────────────────────

# Twitter/X handler

# ─────────────────────────────────────────────

def handle_twitter(url: str) -> dict:
encoded = urllib.parse.quote(url, safe=””)
formats = [
{
“quality”: “COBALT”,
“label”: “Twitter · X Videos”,
“url”: f”https://cobalt.tools/?u={encoded}”,
“type”: “web”,
“recommended”: True,
},
{
“quality”: “SXDL”,
“label”: “Twitter Downloader”,
“url”: f”https://sxdl.net/?url={encoded}”,
“type”: “web”,
},
{
“quality”: “TWITTERVID”,
“label”: “HD Quality”,
“url”: f”https://twittervid.com/?url={encoded}”,
“type”: “web”,
},
]
return {
“platform”: “Twitter/X”,
“title”: “Twitter/X Video”,
“author”: “”,
“thumbnail”: “”,
“formats”: formats,
}

# ─────────────────────────────────────────────

# Facebook handler

# ─────────────────────────────────────────────

def handle_facebook(url: str) -> dict:
encoded = urllib.parse.quote(url, safe=””)
formats = [
{
“quality”: “GETFVID”,
“label”: “Facebook Video DL”,
“url”: f”https://www.getfvid.com/?url={encoded}”,
“type”: “web”,
“recommended”: True,
},
{
“quality”: “FDOWN”,
“label”: “HD · SD”,
“url”: f”https://fdown.net/?url={encoded}”,
“type”: “web”,
},
{
“quality”: “COBALT”,
“label”: “Universal”,
“url”: f”https://cobalt.tools/?u={encoded}”,
“type”: “web”,
},
]
return {
“platform”: “Facebook”,
“title”: “Facebook Video”,
“author”: “”,
“thumbnail”: “”,
“formats”: formats,
}

# ─────────────────────────────────────────────

# Generic handler

# ─────────────────────────────────────────────

def handle_other(url: str) -> dict:
encoded = urllib.parse.quote(url, safe=””)
formats = [
{
“quality”: “COBALT”,
“label”: “Universal Downloader”,
“url”: f”https://cobalt.tools/?u={encoded}”,
“type”: “web”,
“recommended”: True,
},
{
“quality”: “SAVEFROM”,
“label”: “1000+ Sites”,
“url”: f”https://en.savefrom.net/#url={encoded}”,
“type”: “web”,
},
{
“quality”: “LOADER.TO”,
“label”: “Multi-platform”,
“url”: f”https://loader.to/en/tool/?url={encoded}”,
“type”: “web”,
},
]
return {
“platform”: “Video”,
“title”: “Video”,
“author”: “”,
“thumbnail”: “”,
“formats”: formats,
}

# ─────────────────────────────────────────────

# Main dispatcher

# ─────────────────────────────────────────────

def process_url(url: str) -> dict:
platform = detect_platform(url)
handlers = {
“youtube”: handle_youtube,
“instagram”: handle_instagram,
“tiktok”: handle_tiktok,
“twitter”: handle_twitter,
“facebook”: handle_facebook,
“other”: handle_other,
}
return handlers[platform](url)

# ─────────────────────────────────────────────

# Vercel handler

# ─────────────────────────────────────────────

class handler(BaseHTTPRequestHandler):

```
def do_OPTIONS(self):
    self.send_response(200)
    self._cors()
    self.end_headers()

def do_GET(self):
    parsed = urllib.parse.urlparse(self.path)
    params = urllib.parse.parse_qs(parsed.query)

    if parsed.path != "/api/download":
        self._json({"error": "Not found"}, 404)
        return

    url = params.get("url", [None])[0]
    if not url:
        self._json({"error": "url parameter required"}, 400)
        return

    try:
        data = process_url(url)
        self._json({"success": True, "data": data})
    except ValueError as e:
        self._json({"error": str(e)}, 422)
    except Exception as e:
        self._json({"error": "Server error. Dobara try karein."}, 500)

def _cors(self):
    self.send_header("Access-Control-Allow-Origin", "*")
    self.send_header("Access-Control-Allow-Methods", "GET, OPTIONS")
    self.send_header("Access-Control-Allow-Headers", "Content-Type")

def _json(self, data: dict, status: int = 200):
    body = json.dumps(data).encode("utf-8")
    self.send_response(status)
    self._cors()
    self.send_header("Content-Type", "application/json")
    self.send_header("Content-Length", str(len(body)))
    self.end_headers()
    self.wfile.write(body)

def log_message(self, *args):
    pass
```