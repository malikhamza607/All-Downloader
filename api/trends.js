export default async function handler(req, res) {
    // Tumhari RapidAPI ki details yahan use hongi
    const options = {
        method: 'GET',
        headers: {
            'X-RapidAPI-Key': process.env.RAPIDAPI_KEY, // Vercel me set karenge
            'X-RapidAPI-Host': 'your-chosen-tiktok-api.p.rapidapi.com' // RapidAPI se copy karein
        }
    };

    try {
        // Yeh URL us API par depend karega jo tum RapidAPI par select karoge
        // Misaal ke taur par region 'PK' (Pakistan) pass kar rahe hain
        const response = await fetch('https://your-chosen-tiktok-api.p.rapidapi.com/trending/sounds?region=PK', options);
        const data = await response.json();

        // API se aane wale data ko apne hisaab se map karein
        // Yeh structure API ke response ke hisaab se change ho sakta hai
        const formattedSounds = data.map(sound => ({
            name: sound.title || "Unknown Sound",
            uses: sound.playCount ? `${(sound.playCount / 1000000).toFixed(1)}M Videos` : "Trending"
        })).slice(0, 5); // Sirf top 5 sounds

        res.status(200).json(formattedSounds);
    } catch (error) {
        console.error(error);
        res.status(500).json({ error: 'Failed to fetch trending data' });
    }
}
