from flask import Flask, render_template, url_for

site_data = {
    "name": "Ragul R",
    "skills": ["Python", "Flask", "SQL", "Docker", "AWS"],
    "available_for_hire": True,
    "projects": [
        {
            "title": "Portfolio Website",
            "description": "A responsive personal portfolio built with Flask and Jinja2.",
            "tech": ["Flask", "Jinja2", "HTML", "CSS"],
        },
        {
            "title": "API Service",
            "description": "RESTful API with authentication and rate limiting.",
            "tech": ["FastAPI", "PostgreSQL", "Redis"],
        },
        {
            "title": "Data Pipeline",
            "description": "ETL pipeline for analytics with scheduled workflows.",
            "tech": ["Airflow", "Pandas", "S3"],
        },
    ],
}

def create_app():
    app = Flask(__name__)

    @app.context_processor
    def inject_site_data():
        return dict(
            site_name=site_data["name"],
            skills=site_data["skills"],
            available_for_hire=site_data["available_for_hire"],
        )

    @app.route("/")
    def home():
        return render_template(
            "home.html",
            projects=site_data["projects"],
        )

    @app.route("/about")
    def about():
        return render_template("about.html")

    @app.route("/projects")
    def projects():
        return render_template("projects.html", projects=site_data["projects"])

    @app.route("/contact")
    def contact():
        return render_template("contact.html")

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)