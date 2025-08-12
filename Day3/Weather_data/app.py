from flask import Flask, render_template, url_for

def create_app():
    app = Flask(__name__)

    @app.route("/weather")
    def weather():
        # Example payload for "today"
        today = {
            "city": "Chennai",
            "temperature": 33,  
            "condition": "rain",  
            "hours": ["6 AM", "9 AM", "12 PM", "3 PM", "6 PM", "9 PM"],
            "temps": [24, 28, 33, 35, 31, 27],
        }
        return render_template("weather.html", today=today)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
