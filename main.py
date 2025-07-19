from flask import Flask, render_template, request, jsonify
import json
from fuzzywuzzy import process

app = Flask(__name__)

# Debug line to confirm location of file
import os
print("Looking for intents.json at:", os.path.abspath("intents.json"))

# Load intents
with open("intents.json", "r", encoding="utf-8") as file:
    intents = json.load(file)["intents"]

def get_best_response(user_query):
    all_patterns = {}
    for intent in intents:
        for pattern in intent["patterns"]:
            all_patterns[pattern] = intent["responses"]

    best_match, confidence = process.extractOne(user_query, list(all_patterns.keys()))
    if best_match and confidence > 60:
        return all_patterns[best_match][0]
    return "Sorry, I didn't understand that. Can you rephrase?"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get_response", methods=["POST"])
def get_response():
    user_query = request.json.get("message").lower()
    response = get_best_response(user_query)
    return jsonify({"response": response})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
