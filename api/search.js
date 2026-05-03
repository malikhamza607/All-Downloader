export default async function handler(req, res) {
    if (req.method !== 'GET') {
        return res.status(405).json({ error: 'Method Not Allowed' });
    }

    const { query } = req.query;

    if (!query) {
        return res.status(400).json({ error: 'Query is required' });
    }

    // YEH LINE MAIN HAI - Yahan pehle '/search?query=' tha, ab isko '/hashtag?hashtag=' kar diya hai taake videos aayein
    const url = `https://instagram-looter2.p.rapidapi.com/hashtag?hashtag=${query}`;

    const options = {
        method: 'GET',
        headers: {
            'X-RapidAPI-Key': '07e23ed9dbmsh948471f391f4f0fp10ef2bjsn55cdc8e01ce5', 
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
