export default async function handler(req, res) {
    // Tumhari details jo screenshot mein thin
    const options = {
        method: 'GET',
        headers: {
            'x-rapidapi-key': '07e23ed9dbmsh948471f391f4f0fp10ef2bjsn55cdc8e01ce5',
            'x-rapidapi-host': 'tiktok-trending1.p.rapidapi.com'
        }
    };

    try {
        // Trending Feed endpoint for Pakistan (PK)
        // Is se humein trending videos ka data milega jis se hum sounds nikalenge
        const url = 'https://tiktok-api23.p.rapidapi.com/api/trending/feed?region=PK&count=20';
        
        const response = await fetch(url, options);
        const data = await response.json();

        // Agar API se data mil jata hai toh usay agay bhej do
        if (data && (data.itemList || data.data)) {
            res.status(200).json(data);
        } else {
            res.status(404).json({ error: 'Koi trending data nahi mila' });
        }
        
    } catch (error) {
        console.error("Backend Error:", error);
        res.status(500).json({ error: 'TikTok API se connect karne mein masla aya' });
    }
}
