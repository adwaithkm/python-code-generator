# /api/generateCode.py

from transformers import AutoTokenizer, AutoModelForCausalLM
import json

# Set up the model and tokenizer (Adjust the checkpoint if needed)
def handler(request):
    try:
        # Initialize model checkpoint
        checkpoint = "Salesforce/codegen2-1B"
        
        # Load tokenizer and model
        tokenizer = AutoTokenizer.from_pretrained(checkpoint)
        model = AutoModelForCausalLM.from_pretrained(checkpoint)
        
        # Extract the prompt from the request JSON
        request_data = request.get_json()
        prompt = request_data.get("prompt", "")

        # If no prompt is provided, return an error
        if not prompt:
            return json.dumps({"error": "No prompt provided"}), 400

        # Tokenize the input prompt
        input_ids = tokenizer(prompt, return_tensors="pt").input_ids

        # Generate code with a limit on the response length
        generated_ids = model.generate(input_ids, max_length=100)
        generated_code = tokenizer.decode(generated_ids[0], skip_special_tokens=True)

        # Return the generated code as JSON
        return json.dumps({"code": generated_code}), 200

    except Exception as e:
        # Log the error for diagnostics
        return json.dumps({"error": f"Failed to generate code: {str(e)}"}), 500
