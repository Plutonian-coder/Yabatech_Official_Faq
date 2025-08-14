Yabatech AI Assistant
Project Overview
The Yabatech AI Assistant is a web-based chatbot designed to provide instant and accurate information to students and prospective students of Yaba College of Technology. It is built to answer common questions related to admissions, school fees, academic programs, and campus life, leveraging an AI model to provide helpful and conversational responses.

The project consists of a Flask backend that handles the AI logic and API requests, and a simple, responsive frontend built with HTML, CSS, and JavaScript.

Features
Conversational AI: The chatbot can understand and respond to natural language questions.

Knowledge Base: The AI is trained on a specific knowledge base (knowledge.txt) and structured data (data.json) about Yabatech.

Persistent Chat History: The application uses browser cookies to maintain a history of the conversation, allowing for a more natural back-and-forth interaction.

Simple User Interface: The frontend is a clean, modern, and mobile-friendly interface.

Seamless Integration: The frontend and backend are tightly integrated via a simple API endpoint.

Technology Stack
Backend: Python with Flask

AI: Google Gemini (as specified in ai_bot.py)

Frontend: HTML5, CSS3, JavaScript

Package Management: pip with requirements.txt

Project Structure
The project is organized into a few key files:

app.py: The main Flask application file that defines the web server and the /ask API route.

ai_bot.py: Contains the core AI logic, including the setup of the language model and the LangGraph state machine.

knowledge.txt: A text file containing the knowledge base used to train the AI.

data.json: A JSON file with structured data about the school, such as cut-off marks and school fees.

requirements.txt: Lists all the Python dependencies required for the project.

env: The environment file containing the GEMINI_API_KEY.

templates/index.html: The main frontend file, including the HTML structure and embedded CSS and JavaScript.

static/style.css: (If you use a separate style file)

static/script.js: (If you use a separate script file)

Getting Started
Follow these steps to set up and run the project locally.

Prerequisites
Python 3.8+ installed on your system.

pip for installing Python packages.

A Google Gemini API key.

1. Clone the Repository
First, clone this repository to your local machine using Git.

git clone https://github.com/your-username/your-repo-name.git
cd yabatech-ai-assistant

2. Set Up the Environment
Create a .env file in the root directory of your project and add your Gemini API key.

.env

GEMINI_API_KEY="YOUR_API_KEY_HERE"

3. Install Dependencies
Install all the required Python packages using the requirements.txt file.

pip install -r requirements.txt

4. Run the Application
Start the Flask development server by running app.py.

python app.py

The server will start on http://127.0.0.1:4000 or a similar port.

Usage
Open your web browser and navigate to the local host address provided by the Flask server (e.g., http://127.0.0.1:4000).

The Yabatech AI Assistant will appear on the page.

Click the chatbot icon to open the chat window.

Type your questions into the input field and press Send or Enter to get a response. The conversation history will be saved in your browser.

Contributing
We welcome contributions to this project! If you have suggestions or want to improve the chatbot, please follow these steps:

Fork the repository.

Create a new branch (git checkout -b feature/amazing-feature).

Commit your changes (git commit -m 'Add some amazing feature').

Push to the branch (git push origin feature/amazing-feature).

Open a Pull Request.

License
This project is licensed under the MIT License.