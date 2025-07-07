from flask import Flask, request, jsonify
import pyttsx3

app = Flask(__name__)
tts = pyttsx3.init()

@app.route("/respond", methods=["POST"])
def respond():
    data = request.get_json()
    prompt = data.get("text", "")
    response = f"LUMIÆ is thinking about: {prompt}"
    return jsonify({"response": response})

@app.route("/speak", methods=["POST"])
def speak():
    data = request.get_json()
    text = data.get("text", "")
    tts.say(text)
    tts.runAndWait()
    return jsonify({"status": "spoken"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
