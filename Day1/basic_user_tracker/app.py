from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h2>Welcome to the User Tracker App</h2><p>Try /user/yourname</p>"

@app.route('/user/<name>')
def greet_user(name):
    print(f"[INFO] /user/{name} accessed")
    return f"<h3>Welcome, {name.capitalize()}!</h3>"

@app.route('/user/<name>/location/<city>')
def user_location(name, city):
    print(f"[INFO] /user/{name}/location/{city} accessed")
    return f"<p>Hi {name.capitalize()}, how is <b>{city.capitalize()}</b>?</p>"

if __name__ == '__main__':
    app.run(debug=True)
