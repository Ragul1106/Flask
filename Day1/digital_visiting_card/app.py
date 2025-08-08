from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <h1>Ragul R</h1>
    <p>Full Stack Developer & Designer</p>
    <p>Contact: ragul@example.com | +91 9876543210</p>
    """

@app.route('/about')
def about():
    return "<p>I have a background in software engineering and UI/UX design.</p>"

@app.route('/skills/<name>')
def skills(name):
    return f"<p>Skills of {name.title()}: Python, Flask, React, Figma, SQL</p>"

if __name__ == '__main__':
    app.run(debug=True)
