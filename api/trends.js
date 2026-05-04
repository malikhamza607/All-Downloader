export default async function handler(req, res) {
    // CORS headers taake frontend par error na aaye
    res.setHeader('Access-Control-Allow-Credentials', true);
    res.setHeader('Access-Control-Allow-Origin', '*');
    res.setHeader('Access-Control-Allow-Methods', 'GET,OPTIONS,PATCH,DELETE,POST,PUT');

    const options = {
        method: 'GET',
        headers: {
            'x-rapidapi-key': '07e23ed9dbmsh948471f391f4f0fp10ef2bjsn55cdc8e01ce5', // Tumhari key
            'x-rapidapi-host': 'tiktok-api23.p.rapidapi.com'
        }
    };

    try {
        // Humne yahan country=US kar diya hai test karne ke liye
        const url = 'https://tiktok-api23.p.rapidapi.com/api/music/trending?country=US'; 
        
        const response = await fetch(url, options);
        const data = await response.json();

        // Data ko frontend ki taraf bhej rahe hain
        res.status(200).json(data);
        
    } catch (error) {
        console.error("Backend Error:", error);
        res.status(500).json({ error: 'Connection error! US data bhi fetch nahi ho saka.' });
    }
}
