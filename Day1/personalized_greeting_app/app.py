from flask import Flask

app = Flask(__name__)

@app.route('/hello/<name>')
def hello(name):
    return f"<h2>Hello, {name.title()}!</h2>"

@app.route('/greet/<name>/<time>')
def greet(name, time):
    time = time.lower()
    greeting = "Good Morning" if "morning" in time else "Good Evening"
    return f"<p>{greeting}, {name.title()}!</p>"

if __name__ == '__main__':
    app.run(debug=True)
