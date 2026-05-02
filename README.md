# VidSnatch — Video Downloader

YouTube, Instagram, TikTok, Twitter/X, Facebook video downloader built with Python (yt-dlp) + Vercel.

## Project Structure

```
video-downloader/
├── api/
│   └── download.py      ← Vercel serverless Python function
├── index.html           ← Frontend UI
├── requirements.txt     ← Python dependencies
├── vercel.json          ← Vercel config
└── README.md
```

## Deploy on Vercel (Step by Step)

### 1. Prerequisites

- [Vercel account](https://vercel.com) (free)
- [GitHub account](https://github.com)
- [Node.js](https://nodejs.org) installed (for Vercel CLI)

### 2. Install Vercel CLI

```bash
npm install -g vercel
```

### 3. Upload to GitHub

```bash
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/YOUR_USERNAME/video-downloader.git
git push -u origin main
```

### 4. Deploy to Vercel

```bash
vercel login
vercel --prod
```

Or connect via Vercel Dashboard:

1. Go to https://vercel.com/new
1. Import your GitHub repo
1. Click **Deploy** — done!

## How It Works

1. User pastes a video URL
1. Frontend calls `/api/download?url=VIDEO_URL`
1. Python serverless function uses **yt-dlp** to extract all available formats
1. Frontend shows quality options (720p, 480p, 360p, etc.)
1. User clicks → direct browser download

## Supported Platforms

- ✅ YouTube
- ✅ Instagram (public posts/reels)
- ✅ TikTok
- ✅ Twitter / X
- ✅ Facebook (public videos)
- ✅ 1000+ other sites supported by yt-dlp

## Notes

- Private/age-restricted videos may not work
- Instagram private accounts won’t work
- For personal use only — respect copyright