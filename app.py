import requests

DEEPSEEK_API_KEY = "sk-07d47b3a5f604ce1984f7734c9ab7ae7"
DEEPSEEK_API_URL = "https://api.deepseek.com/v1/chat/completions"

@app.route('/respond', methods=['POST'])
def respond():
    data = request.get_json()
    user_text = data.get('text', '')

    # Send to DeepSeek for smart AI reply
    headers = {
        "Authorization": f"Bearer {DEEPSEEK_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "deepseek-chat",  # or "deepseek-coder" if you want it to write code
        "messages": [
            {"role": "system", "content": "You are LUMIÆ, a smart assistant who responds like a human friend."},
            {"role": "user", "content": user_text}
        ]
    }

    try:
        res = requests.post(DEEPSEEK_API_URL, headers=headers, json=payload)
        result = res.json()
        reply = result["choices"][0]["message"]["content"].strip()
    except Exception as e:
        print("❌ DeepSeek error:", e)
        reply = "Sorry, I'm having trouble thinking right now. 😞"

    # Save to DB (optional if you want memory)
    with sqlite3.connect(DB) as conn:
        conn.execute("INSERT INTO chat (timestamp, user_text, bot_response) VALUES (?, ?, ?)",
                     (time.time(), user_text, reply))

    return jsonify({"response": reply})
