FROM python:3.9-slim

WORKDIR /app

# Copy only requirements first for caching
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn", "generateCode:app", "--host", "0.0.0.0", "--port", "8000"]
