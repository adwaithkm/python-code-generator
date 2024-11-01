// api/openai.js

import axios from 'axios';

export default async function handler(req, res) {
    if (req.method === 'POST') {
        const { prompt } = req.body; // Get the prompt from the request body

        try {
            // Call the OpenAI API
            const response = await axios.post('https://api.openai.com/v1/chat/completions', {
                model: 'gpt-3.5-turbo', // Specify the model
                messages: [{ role: 'user', content: `Generate Python code for: ${prompt}` }],
            }, {
                headers: {
                    'Authorization': `Bearer ${process.env.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}`, // Use the API key from environment variables
                    'Content-Type': 'application/json',
                }
            });

            // Send back the response from OpenAI
            res.status(200).json({ response: response.data.choices[0].message.content });
        } catch (error) {
            // Handle errors from OpenAI API
            console.error(error);
            res.status(500).json({ error: 'Error communicating with OpenAI API' });
        }
    } else {
        // If the request method is not POST, return a 405 Method Not Allowed
        res.setHeader('Allow', ['POST']);
        res.status(405).end(`Method ${req.method} Not Allowed`);
    }
}
