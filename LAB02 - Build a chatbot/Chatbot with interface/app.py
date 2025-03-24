from flask import Flask, render_template, request, jsonify
from transformers import BlenderbotTokenizer, BlenderbotForConditionalGeneration

# Load the BlenderBot model and tokenizer
model_name = "facebook/blenderbot-400M-distill"
tokenizer = BlenderbotTokenizer.from_pretrained(model_name)
model = BlenderbotForConditionalGeneration.from_pretrained(model_name)

# Initialize Flask
app = Flask(__name__)

# Function to handle the conversation
def chatbot(user_input):
    # Encode the user input
    inputs = tokenizer(user_input, return_tensors="pt")

    # Generate the model's response
    reply_ids = model.generate(**inputs, max_length=200)

    # Decode the generated response
    response = tokenizer.decode(reply_ids[0], skip_special_tokens=True)
    return response

# Main route to render the chatbot page
@app.route('/')
def index():
    # Render the HTML file for the frontend
    return render_template('chat.html')

# Route to handle chatbot responses
@app.route('/chat', methods=['POST'])
def chat():
    # Get the user input from the request
    user_input = request.json.get("message", "")
    try:
        # Generate a response using the chatbot function
        response = chatbot(user_input)
        # Return the response as JSON
        return jsonify({"response": response})
    except Exception as e:
        # Handle any errors and return an error message
        return jsonify({"response": f"Error: {str(e)}"}), 500

# Run the application
if __name__ == '__main__':
    # Start the Flask app in debug mode
    app.run(debug=True)