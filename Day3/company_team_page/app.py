from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def team():
    team_members = [
        {
            "name": "Ragul",
            "role": "Team Lead",
            "photo": "member1.jpeg"
        },
        {
            "name": "Ranjith",
            "role": "Developer",
            "photo": "member2.jpeg"
        },
        {
            "name": "Heera",
            "role": "Designer",
            "photo": "member3.png"
        }
    ]
    return render_template("team.html", title="Our Team", team=team_members)

if __name__ == "__main__":
    app.run(debug=True)
