from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
from flask import Flask, request, jsonify

# Set up the model and tokenizer
checkpoint = "Salesforce/codegen2-1B"
device = "cuda" if torch.cuda.is_available() else "cpu"
tokenizer = AutoTokenizer.from_pretrained(checkpoint)
model = AutoModelForCausalLM.from_pretrained(checkpoint).to(device)

app = Flask(__name__)

@app.route('/api/generateCode', methods=['POST'])
def generate_code():
    data = request.json
    prompt = data.get('prompt')
    input_ids = tokenizer(prompt, return_tensors="pt").input_ids.to(device)
    generated_ids = model.generate(input_ids, max_length=1024)
    generated_code = tokenizer.decode(generated_ids[0], skip_special_tokens=True)
    return jsonify({"code": generated_code})

# Entry point for Vercel
def handler(request):
    return app(request)
