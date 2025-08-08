from flask import Flask
import random

app = Flask(__name__)

messages = [
    "Believe in yourself!",
    "You are capable of amazing things.",
    "Never give up.",
    "Push through the challenges.",
    "Success is a journey.",
    "Dream big, work hard.",
    "Stay positive and strong!"
]

@app.route("/message")
def random_message():
    message = random.choice(messages)
    return f"""
    <h1 style='color: teal; font-family: Arial;'>{message}</h1>
    """

@app.route("/message/<int:index>")
def specific_message(index):
    if 0 <= index < len(messages):
        return f"<h2 style='color: purple; font-family: Arial;'>{messages[index]}</h2>"
    return "<p style='color: red;'>Invalid index. Try 0 to 6.</p>"

if __name__ == "__main__":
    app.run(debug=True)
