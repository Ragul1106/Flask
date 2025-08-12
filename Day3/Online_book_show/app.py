from flask import Flask, render_template, url_for

books_data = [
    {
        "name": "The Psychology of Money",
        "author": "Howard Marks",
        "cover": "images/b1.jpeg",
    },
    {
        "name": "The Story of Money",
        "author": "Sean Cover",
        "cover": "images/b2.jpg",
    },
    {
        "name": "The Money River",
        "author": "Zoe M. Hicks",
        "cover": "images/b3.png",
    },
]

def create_app():
    app = Flask(__name__)

    @app.route("/books")
    def books():
        return render_template("books.html", books=books_data)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)