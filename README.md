# Yabatech AI Assistant

## 📌 Project Overview
The **Yabatech AI Assistant** is a web-based chatbot designed to provide instant and accurate information to students and prospective students of **Yaba College of Technology**.  
It answers common questions related to **admissions, school fees, academic programs, and campus life**, leveraging an AI model for helpful and conversational responses.

The project consists of:
- **Flask backend** – Handles AI logic and API requests.
- **Responsive frontend** – Built with HTML, CSS, and JavaScript.

---

## ✨ Features
- **Conversational AI** – Understands and responds to natural language.
- **Knowledge Base** – Uses `knowledge.txt` and `data.json` with Yabatech-specific info.
- **Persistent Chat History** – Maintains conversation context using browser cookies.
- **Simple UI** – Clean, modern, and mobile-friendly.
- **Seamless Integration** – Frontend and backend connected via a simple API.

---

## 🛠 Technology Stack
- **Backend:** Python + Flask  
- **AI Model:** Google Gemini (configured in `ai_bot.py`)  
- **Frontend:** HTML5, CSS3, JavaScript  
- **Package Management:** pip (`requirements.txt`)

---

## 📂 Project Structure
app.py # Main Flask application & API routes
ai_bot.py # AI logic & Gemini integration
knowledge.txt # AI knowledge base
data.json # Structured school data
requirements.txt # Python dependencies
.env # Environment variables (GEMINI_API_KEY)
templates/index.html # Main frontend HTML
static/style.css # Optional CSS file
static/script.js # Optional JavaScript file

yaml
Copy
Edit

---

## 🚀 Getting Started

### **Prerequisites**
- Python **3.8+**
- pip
- Google Gemini API Key

### **Clone the Repository**
```bash
git clone https://github.com/your-username/your-repo-name.git
cd yabatech-ai-assistant
Set Up Environment
Create a .env file:

env
Copy
Edit
GEMINI_API_KEY="YOUR_API_KEY_HERE"
Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
Run the Application
bash
Copy
Edit
python app.py
Server runs at: http://127.0.0.1:4000