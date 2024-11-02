
# FastAPI Code Generation App

This is a FastAPI application that uses Groq’s API to generate code based on user input. This application serves a frontend HTML file and provides an API endpoint for code generation. It leverages the `Groq` API client to generate Python code based on a user-provided description.

## Table of Contents

1. [Requirements](#requirements)
2. [Installation](#installation)
3. [Configuration](#configuration)
4. [Usage](#usage)
5. [API Endpoints](#api-endpoints)
6. [Running the Application](#running-the-application)
7. [Security Note](#security-note)
8. [Troubleshooting](#troubleshooting)

---

## Requirements

- Python 3.7 or above
- `FastAPI` framework
- `Uvicorn` ASGI server
- `Groq` API client

## Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/fastapi-code-generation-app.git
   cd fastapi-code-generation-app
   ```

2. **Install Dependencies**
   Ensure you are in the project directory, then install the necessary packages:
   ```bash
   pip install fastapi uvicorn groq
   ```

## Configuration

This application requires a Groq API key for code generation. Replace the placeholder API key in the code with your actual API key.

```python
client = Groq(api_key='your_actual_api_key_here')
```

**Note**: For production environments, avoid hardcoding the API key directly in your code. Use environment variables or a configuration management system to manage secrets securely.

## Usage

1. **Serve the Frontend**
   - The root endpoint (`/`) serves the `index.html` file located in the `static` folder.
   - You can modify this HTML file to customize the frontend of the application.

2. **Generate Code with Groq API**
   - Use the `/generate_code/` endpoint to generate Python code based on a description you provide.
   - The endpoint accepts a JSON payload with a `description` key.

## API Endpoints

### `GET /`

Serves the `index.html` file from the `static` directory.

- **Response**: HTML content from `index.html`.

### `POST /generate_code/`

Generates Python code based on the description provided by the user.

- **Request Body**:
  ```json
  {
    "description": "Describe what you want the code to do"
  }
  ```
- **Response**:
  ```json
  {
    "code": "Generated Python code here"
  }
  ```

### Error Handling

The application provides error handling to ensure robust responses:

- **400 Bad Request**: Missing or invalid input.
- **500 Internal Server Error**: Issues with API calls or internal failures.

## Running the Application

Start the application with Uvicorn by running the following command:

```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

Once the server is running, visit [http://localhost:8000](http://localhost:8000) to access the frontend.

## Security Note

**Important**: This application directly includes the API key in the code for testing purposes only. For production, ensure you:

- Store the API key securely, ideally in environment variables.
- Avoid committing sensitive information like API keys to version control.

## Troubleshooting

- **Error: `FileNotFoundError` for `index.html`**: Make sure the `static` directory exists in the project root and contains `index.html`.
- **API Connection Errors**: Check if the Groq API key is valid and your internet connection is stable.
- **CORS Issues**: If deploying this application on a different domain, configure CORS as needed in FastAPI.
