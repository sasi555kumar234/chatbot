from flask import Flask, request, jsonify
from flask import Flask, request, jsonify, render_template
import random

app = Flask(__name__)

# Mock product data
products = [
    {"id": 1, "name": "Laptop", "price": 999.99},
    {"id": 2, "name": "Smartphone", "price": 499.99},
    {"id": 3, "name": "Headphones", "price": 199.99},
    {"id": 4, "name": "Smartwatch", "price": 299.99},
    {"id": 5, "name": "Tablet", "price": 399.99},
    # Add more products as needed
]
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    response_message = generate_response(user_message)
    return jsonify({"response": response_message})


def generate_response(message):
    # Normalize the message to lower case for easier matching
    message = message.lower()
    if "price" in message:
        for product in products:
            if product['name'].lower() in message:
                return f"The price of the {product['name']} is ${product['price']}."
    
    # Check for keywords in the user's message
    if "product" in message:
        product = random.choice(products)
        return f"How about a {product['name']} for ${product['price']}?"
    elif "recommend" in message:
        product = random.choice(products)
        return f"I recommend the {product['name']} for you!"
    elif "hello" in message or "hi" in message:
        return "Hello! How can I assist you today?"
    elif "help" in message:
        return "Sure! You can ask me about our products or request a recommendation."
    else:
        return "I'm here to help! Ask me about our products or say 'help' for assistance."

if __name__ == '__main__':
    app.run(debug=True)