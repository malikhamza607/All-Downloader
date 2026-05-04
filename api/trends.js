export default async function handler(req, res) {
    const options = {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
            'x-rapidapi-host': 'tiktok-api23.p.rapidapi.com',
            // Note: Screenshot mein tumhari API key show ho rahi thi, maine wahi yahan daal di hai
            // Lekin hamesha koshish karo ke API key environment variables (process.env) mein rakho
            'x-rapidapi-key': '07e23ed9dbmsh948471f391f4f0fp10ef2bjsn55cdc8e01ce5' 
        }
    };

    try {
        // Screenshot wala exact URL aur parameters
        const url = 'https://tiktok-api23.p.rapidapi.com/api/user/oldest-posts?secUid=MS4wLjABAAAAqB08cUbXaDWqbD6MCga2RbGTuhfO2EsHayBYx08NDrN7IE3jqURDNNN6YwyfH6_6&count=30&cursor=0';
        
        const response = await fetch(url, options);
        const data = await response.json();

        // Frontend ko successfully data bhej do
        res.status(200).json(data);
        
    } catch (error) {
        console.error("Error agaya:", error);
        res.status(500).json({ error: 'TikTok API se data fetch karne mein masla aya' });
    }
}
