export default async function handler(req, res) {
    if (req.method !== 'GET') {
        return res.status(405).json({ error: 'Method Not Allowed' });
    }

    const { query } = req.query;

    if (!query) {
        return res.status(400).json({ error: 'Query is required' });
    }

    // Instagram Looter2 API ka URL
    const url = `https://instagram-looter2.p.rapidapi.com/search?query=${query}`;

    const options = {
        method: 'GET',
        headers: {
            'X-RapidAPI-Key': process.env.RAPIDAPI_KEY, 
            'X-RapidAPI-Host': 'instagram-looter2.p.rapidapi.com'
        }
    };

    try {
        const response = await fetch(url, options);
        
        if (!response.ok) {
            const errorText = await response.text();
            return res.status(response.status).json({ error: 'RapidAPI request failed', details: errorText });
        }

        const data = await response.json();
        res.status(200).json(data);
        
    } catch (error) {
        res.status(500).json({ error: 'Server Crash', details: error.message });
    }
}
