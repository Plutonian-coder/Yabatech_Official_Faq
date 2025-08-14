# app.py
# This is the main Flask application file.
# It handles the web routes and integrates the chatbot logic from ai_bot.py.

import json
import os
from flask import Flask, render_template, request, jsonify, session
from dotenv import load_dotenv # Import to load environment variables
from flask_cors import CORS

# Assuming ai_bot.py contains both get_response for chat and guided_learning_response for the new feature
from ai_bot import get_response, guided_learning_response 

# Initialize the Flask application
app = Flask(__name__, static_folder='static', template_folder='templates')
CORS(app)
# A secret key is needed to manage sessions for chat history
app.secret_key = os.urandom(24) 

# Load environment variables from a .env file
load_dotenv()

# Get the Gemini API key from the environment variable
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY not found in environment variables. "
                     "Please create a .env file with GEMINI_API_KEY=YOUR_API_KEY.")

# --- Routes for all pages ---

@app.route('/')
def home():
    """
    Renders the home page of the application.
    """
    return render_template('home.html')

@app.route('/about')
def about():
    """
    Renders the about page.
    """
    return render_template('about.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    """
    Renders the contact page and handles form submissions.
    """
    if request.method == 'POST':
        # Simple print statement to show form data has been received.
        # In a real application, you would handle this data more securely.
        name = request.form.get('name')
        email = request.form.get('email')
        subject = request.form.get('subject')
        message = request.form.get('message')
        print(f"Contact form submitted by {name} ({email}). Subject: {subject}. Message: {message}")
        return "<h1>Thank you for your message!</h1><p>We will get back to you shortly.</p>"
    return render_template('contact.html')

@app.route('/chatbot')
def chatbot():
    """
    Renders the main chatbot interface page.
    Initializes a new chat history in the session for the user.
    """
    session['chat_history'] = []
    return render_template('chatbot.html')

@app.route('/ask', methods=['POST'])
def ask():
    """
    API endpoint for the chatbot functionality.
    It receives a message, processes it using the AI bot logic, and returns a response.
    """
    user_input = request.json.get('message')
    
    # Retrieve the chat history from the session, or initialize if it doesn't exist
    chat_history = session.get('chat_history', [])
    
    # Get the response from the AI bot, passing the chat history and API key
    bot_response = get_response(user_input, chat_history, GEMINI_API_KEY)

    # Update the chat history in the session
    session['chat_history'] = chat_history

    return jsonify({'response': bot_response})

# New route to handle guided learning requests
@app.route('/guided_learning', methods=['POST'])
def guided_learning():
    """
    API endpoint for the guided learning functionality.
    It receives a topic and returns a structured learning plan.
    """
    topic = request.json.get('topic')
    if topic:
        # Pass the topic to the new AI function to generate a learning plan
        # The API key is also passed for authentication
        learning_plan = guided_learning_response(topic, GEMINI_API_KEY)
        return jsonify({'response': learning_plan})
    return jsonify({'response': 'Please provide a topic for guided learning.'}), 400

if __name__ == '__main__':
    # Make sure to run the app in debug mode only for development.
    # The port is set to 4000 to match the other provided files.
    app.run(debug=True, port=4000)
