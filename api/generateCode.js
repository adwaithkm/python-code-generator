// api/generateCode.js

const fetch = require('node-fetch');

module.exports = async (req, res) => {
    if (req.method !== 'POST') {
        return res.status(405).send({ message: 'Only POST requests allowed' });
    }

    const { prompt } = req.body;

    if (!prompt) {
        return res.status(400).send({ message: 'Prompt is required' });
    }

    try {
        // Use the OpenAI API to generate Python code
        const response = await fetch('https://api.openai.com/v1/completions', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${process.env.OPENAI_API_KEY}` // Store API Key securely
            },
            body: JSON.stringify({
                model: "text-davinci-003",
                prompt: `Generate a Python function or code snippet for: ${prompt}`,
                max_tokens: 100,
                temperature: 0.5
            })
        });

        const data = await response.json();
        const code = data.choices[0].text.trim();

        res.status(200).json({ code });

    } catch (error) {
        console.error(error);
        res.status(500).json({ message: 'Failed to generate code' });
    }
};
