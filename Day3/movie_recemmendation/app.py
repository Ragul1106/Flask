from flask import Flask, render_template

app = Flask(__name__)

movies = [
    {
        "title": "The Dark Knight",
        "poster": "dark_knight.jpeg",
        "rating": 5,
        "is_new": False
    },
    {
        "title": "Oppenheimer",
        "poster": "oppenheimer.jpeg",
        "rating": 4,
        "is_new": True
    },
    {
        "title": "Dune: Part Two",
        "poster": "dune2.jpeg",
        "rating": 4,
        "is_new": True
    }
]

@app.route("/movies")
def movie_list():
    return render_template("movies.html", movies=movies)

if __name__ == "__main__":
    app.run(debug=True)
