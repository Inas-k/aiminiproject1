from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# --- Simple Chatbot Logic ---
def chatbot_response(user_input):
    user_input = user_input.lower()

    if "hello" in user_input:
        return "Hi there! How can I help you today?"
    elif "your name" in user_input:
        return "I'm ChatBot, your friendly assistant 🤖."
    elif "how are you" in user_input:
        return "I'm just a bunch of Python code, but I'm feeling great!"
    elif "bye" in user_input:
        return "Goodbye! Have a wonderful day 😊"
    else:
        return "I'm not sure about that. Could you please rephrase?"

# --- Routes ---
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def get_bot_response():
    data = request.get_json()  # get JSON data
    user_msg = data.get("msg", "")
    bot_reply = chatbot_response(user_msg)
    return jsonify({"response": bot_reply})


if __name__ == "__main__":
    app.run(debug=True)
