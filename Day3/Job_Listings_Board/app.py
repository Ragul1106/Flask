from flask import Flask, render_template, url_for

def create_app():
    app = Flask(__name__)
    @app.route("/jobs")
    def jobs():
        jobs_data = [
        {
            "title": "Backend Engineer",
            "company": "Acme Corp",
            "logo": "images/acme.png",
            "location": "Bengaluru, IN",
            "remote": True,
            "type": "Full-time"
        },
        {
            "title": "Frontend Developer",
            "company": "Globex",
            "logo": "images/globex.png",
            "location": "Pune, IN",
            "remote": False,
            "type": "Contract"
        },
        {
            "title": "DevOps Engineer",
            "company": "Initech",
            "logo": "images/initech.jpeg",
            "location": "Remote - India",
            "remote": True,
            "type": "Full-time"
        },
    ]
        return render_template("jobs.html", jobs=jobs_data)

    return app
if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)