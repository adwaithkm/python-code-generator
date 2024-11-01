# Use a lightweight Python image as the base
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy only the requirements file first for better caching
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose the application on port 8000
EXPOSE 8000

# Command to run the application using uvicorn
CMD ["uvicorn", "generateCode:app", "--host", "0.0.0.0", "--port", "8000"]
