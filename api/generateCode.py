from transformers import AutoTokenizer, AutoModelForCausalLM
import json

def handler(request):
    try:
        # Log checkpoint initialization
        print("Initializing checkpoint and model")
        
        # Initialize model checkpoint
        checkpoint = "Salesforce/codegen2-1B"
        
        # Load tokenizer and model
        tokenizer = AutoTokenizer.from_pretrained(checkpoint)
        model = AutoModelForCausalLM.from_pretrained(checkpoint)
        
        print("Model and tokenizer loaded successfully")

        # Parse request data
        request_data = request.get_json()
        prompt = request_data.get("prompt", "")

        if not prompt:
            return json.dumps({"error": "No prompt provided"}), 400

        print(f"Received prompt: {prompt}")

        # Tokenize input
        input_ids = tokenizer(prompt, return_tensors="pt").input_ids

        # Generate code
        generated_ids = model.generate(input_ids, max_length=100)
        generated_code = tokenizer.decode(generated_ids[0], skip_special_tokens=True)

        print("Code generation successful")

        # Return the generated code
        return json.dumps({"code": generated_code}), 200

    except Exception as e:
        # Capture and log errors in detail
        print(f"Error during code generation: {str(e)}")
        return json.dumps({"error": f"Failed to generate code: {str(e)}"}), 500
