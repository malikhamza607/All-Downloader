export default async function handler(req, res) {
    if (req.method !== 'GET') {
        return res.status(405).json({ error: 'Method Not Allowed' });
    }

    const { query } = req.query;

    if (!query) {
        return res.status(400).json({ error: 'Query is required' });
    }

    // Maine nayi API ke hisab se hashtag search ka link khud set kar diya hai
    const url = `https://instagram-cheapest.p.rapidapi.com/api/v1/instagram/hashtag_media?hashtag=${query}`;

    const options = {
        method: 'GET',
        headers: {
            'X-RapidAPI-Key': '07e23ed9dbmsh948471f391f4f0fp10ef2bjsn55cdc8e01ce5', 
            'X-RapidAPI-Host': 'instagram-cheapest.p.rapidapi.com' // Naya Host
        }
    };

    try {
        const response = await fetch(url, options);
        const textData = await response.text();
        
        if (!response.ok) {
            return res.status(response.status).json({ error: 'RapidAPI request failed', details: textData, url_used: url });
        }

        let data;
        try {
            data = JSON.parse(textData);
        } catch(e) {
            return res.status(500).json({ error: 'Invalid JSON format', details: textData });
        }

        res.status(200).json(data);
        
    } catch (error) {
        res.status(500).json({ error: 'Server Crash', details: error.message });
    }
}
