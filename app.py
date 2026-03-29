from flask import Flask, request, jsonify
import google.generativeai as genai
import os

app = Flask(__name__)

# Configure Gemini API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-pro")

@app.route("/", methods=["POST"])
def summarize():
    data = request.get_json()
    text = data.get("text", "")

    if not text:
        return jsonify({"error": "No text provided"}), 400

    prompt = f"Summarize this text in 2-3 lines:\n{text}"

    response = model.generate_content(prompt)

    return jsonify({
        "input": text,
        "summary": response.text
    })

@app.route("/", methods=["GET"])
def home():
    return "AI Agent is running 🚀"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
