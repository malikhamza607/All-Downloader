export default async function handler(req, res) {
    // Frontend ko errors se bachane ke liye CORS headers
    res.setHeader('Access-Control-Allow-Credentials', true);
    res.setHeader('Access-Control-Allow-Origin', '*');
    res.setHeader('Access-Control-Allow-Methods', 'GET,OPTIONS,PATCH,DELETE,POST,PUT');

    // Tumhari RapidAPI details jo pichle screenshots mein thin
    const options = {
        method: 'GET',
        headers: {
            'x-rapidapi-key': '07e23ed9dbmsh948471f391f4f0fp10ef2bjsn55cdc8e01ce5', // Tumhari API Key
            'x-rapidapi-host': 'tiktok-api23.p.rapidapi.com' // Agar host ka naam different ho toh yahan change kar lena
        }
    };

    try {
        // ⚠️ ZAROORI NOTE: Apni RapidAPI screen par right side mein jo "Code Snippets" ka box hai, 
        // wahan se exact URL copy kar ke is line mein paste kar lena agar yeh wali URL kaam na kare.
        const url = 'https://tiktok-api23.p.rapidapi.com/api/music/trending?region=PK'; 
        
        const response = await fetch(url, options);
        const data = await response.json();

        // Frontend ko successfully data bhej do
        res.status(200).json(data);
        
    } catch (error) {
        console.error("Backend Error:", error);
        res.status(500).json({ error: 'TikTok API se connect nahi ho paya. RapidAPI limit ya URL check karo.' });
    }
}
