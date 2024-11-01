import axios from 'axios';

export default async function handler(req, res) {
    if (req.method === 'POST') {
        const { prompt } = req.body; // Get the prompt from the request body

        console.log('Received prompt:', prompt); // Log the prompt for debugging

        try {
            const response = await axios.post('https://api.groq.com/', {
                model: "llama3-8b-8192", // Specify the model to use
                messages: [{
                    role: "user", // Role of the message sender
                    content: prompt // The content of the message
                }]
            }, {
                headers: {
                    'Authorization': `Bearer ${process.env.GROQ_API_KEY}`, // Access the API key here
                    'Content-Type': 'application/json', // Set content type to JSON
                }
            });

            // Send the API response back to the client
            res.status(200).json({ response: response.data });
        } catch (error) {
            // Enhanced error logging
            if (error.response) {
                console.error('Error Response:', error.response.data);
                res.status(error.response.status).json({ error: error.response.data });
            } else {
                console.error('Error Message:', error.message);
                res.status(500).json({ error: 'Error communicating with Groq API' });
            }
        }
    } else {
        // If the method is not POST, return a 405 error
        res.setHeader('Allow', ['POST']);
        res.status(405).end(`Method ${req.method} Not Allowed`);
    }
}

