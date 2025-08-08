from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    hour = datetime.now().hour
    status = "We are open!" if 9 <= hour < 18 else "Closed"
    return f"<h1>{status}</h1>"

@app.route('/contact')
def contact():
    return """
    <b>Email:</b> support@mybiz.com <br>
    <b>Phone:</b> +91 9000000000
    <hr>
    <p>Thank you for contacting us.</p>
    """

if __name__ == '__main__':
    app.run(debug=True)
