from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow cross-origin for frontend requests

# Simple personality modes
PERSONALITIES = {
    "JARVIS": "I am JARVIS, your loyal assistant.",
    "SAMANTHA": "Hi, I'm Samantha. How can I brighten your day?",
    "HAL": "I am HAL 9000. I'm here to help."
}

@app.route('/')
def home():
    return "🌟 LUMIÆ backend is live!"

@app.route('/respond', methods=['POST'])
def respond():
    data = request.get_json()
    text = data.get('text', '').lower()
    mode = data.get('mode', 'JARVIS').upper()

    # Basic AI logic (expandable)
    if "hello" in text:
        reply = f"{PERSONALITIES.get(mode, '')} Hello there!"
    elif "how are you" in text:
        reply = f"{PERSONALITIES.get(mode, '')} I'm doing well, thank you."
    elif "goodbye" in text or "bye" in text:
        reply = f"{PERSONALITIES.get(mode, '')} Goodbye! Talk to you later."
    else:
        reply = f"{PERSONALITIES.get(mode, '')} You said: {text}"

    return jsonify({"response": reply})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
