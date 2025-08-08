from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '<p>Enter your banner text:</p><a href="/banner/Hello">Try Example</a>'

@app.route('/banner/<text>')
def banner(text):
    return f"<h1>{text}</h1>"

@app.route('/banner/<text>/<size>')
def banner_with_size(text, size):
    if size.lower() in ['h1','h2','h3','h4','h5','h6']:
        return f"<{size}>{text}</{size}>"
    return "<p>Invalid size. Use h1 to h6.</p>"

if __name__ == '__main__':
    app.run(debug=True)
