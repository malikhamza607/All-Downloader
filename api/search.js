export default async function handler(req, res) {
    // Sirf GET request allow karein
    if (req.method !== 'GET') {
        return res.status(405).json({ error: 'Method Not Allowed' });
    }

    const { query } = req.query;

    if (!query) {
        return res.status(400).json({ error: 'Query is required' });
    }

    // Yahan RapidAPI ka URL dalna hai (Yeh ek example URL hai)
    const url = `https://instagram-scraper-api2.p.rapidapi.com/v1/search_hashtag?hashtag=${query}`;

    const options = {
        method: 'GET',
        headers: {
            // process.env Vercel ke environment variables se key uthayega
            'X-RapidAPI-Key': process.env.RAPIDAPI_KEY, 
            'X-RapidAPI-Host': 'instagram-scraper-api2.p.rapidapi.com' // Jo host API provider de
        }
    };

    try {
        const response = await fetch(url, options);
        const data = await response.json();
        
        // Frontend ko data bhej do
        res.status(200).json(data);
    } catch (error) {
        res.status(500).json({ error: 'Failed to fetch data from RapidAPI' });
    }
}
