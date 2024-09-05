import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from flask import Flask, request, jsonify
import nltk

# Download NLTK resources
nltk.download('punkt')

# Load pre-trained model and tokenizer
tokenizer = AutoTokenizer.from_pretrained('gpt2')
model = AutoModelForCausalLM.from_pretrained('gpt2')

# Initialize Flask app
app = Flask(__name__)

@app.route('/chatbot', methods=['POST'])
def chatbot_response():
    user_query = request.json.get('query')

    # Tokenize and generate response
    input_ids = tokenizer.encode(user_query, return_tensors='pt')
    output = model.generate(input_ids, max_length=50)
    response = tokenizer.decode(output[0], skip_special_tokens=True)

    return jsonify({'response': response})

if __name__ == "__main__":
    app.run(port=5000)
