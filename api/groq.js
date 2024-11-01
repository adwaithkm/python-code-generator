import axios from 'axios';

export default async function handler(req, res) {
    if (req.method === 'POST') {
        const { prompt } = req.body; // Assuming you send prompt as part of the request body

        try {
            const response = await axios.post('https://api.groq.com/openai/v1/chat/completions', {
                model: "llama3-8b-8192",
                messages: [{
                    role: "user",
                    content: prompt // Use the prompt from the request body
                }]
            }, {
                headers: {
                    'Authorization': `Bearer ${process.env.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}`, // Ensure your API key is stored securely
                    'Content-Type': 'application/json',
                }
            });

            // Send the response data back to the client
            res.status(200).json({ response: response.data });
        } catch (error) {
            console.error(error);
            res.status(500).json({ error: 'Error communicating with Groq API' });
        }
    } else {
        res.setHeader('Allow', ['POST']);
        res.status(405).end(`Method ${req.method} Not Allowed`);
    }
}
