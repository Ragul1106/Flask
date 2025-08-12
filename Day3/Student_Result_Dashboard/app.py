from flask import Flask, render_template, url_for

def create_app():
    app = Flask(__name__)

    @app.route("/result")
    def result():
        student = {
            "name": "Alice Johnson",
            "grade": "A",
            "subjects": [
                {"name": "Tamil", "marks": 99},
                {"name": "Math", "marks": 95},
                {"name": "Science", "marks": 88},
                {"name": "Social", "marks": 76},
                {"name": "English", "marks": 92},
            ],
        }
        return render_template("result.html", student=student, subjects=student["subjects"])

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)