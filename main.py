from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from transformers import pipeline

app = FastAPI()

# Create a model for the request body
class CodeRequest(BaseModel):
    prompt: str

# Load the code generation model
code_generator = pipeline("text-generation", model="EleutherAI/gpt-neo-2.7B")

@app.post("/api/generateCode")
async def generate_code(request: CodeRequest):
    try:
        # Generate code based on the user's prompt
        generated_code = code_generator(request.prompt, max_length=50)
        return {"code": generated_code[0]['generated_text']}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
def read_root():
    return {"message": "Welcome to the Python Code Generator!"}
