from fastapi import FastAPI
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

app = FastAPI()

checkpoint = "Salesforce/codegen2-1B"
device = "cuda" if torch.cuda.is_available() else "cpu"

tokenizer = AutoTokenizer.from_pretrained(checkpoint)
model = AutoModelForCausalLM.from_pretrained(checkpoint, trust_remote_code=True, revision="main")

@app.post("/generateCode/")
async def generate_code(prompt: str):
    input_ids = tokenizer(prompt, return_tensors="pt").input_ids.to(device)
    generated_ids = model.generate(input_ids, max_length=1024)
    code = tokenizer.decode(generated_ids[0], skip_special_tokens=True)
    return {"code": code}
