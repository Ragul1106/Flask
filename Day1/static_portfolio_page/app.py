from flask import Flask

app = Flask(__name__)

profiles = {
    "ragul": {
        "name": "Ragul R",
        "profession": "Full Stack Developer",
        "skills": ["Python", "JavaScript", "React", "Flask", "MySQL"],
        "projects": [
            {"name": "To-Do App", "status": "Completed"},
            {"name": "Wedding Card Store", "status": "Ongoing"}
        ]
    },
    "meenu": {
        "name": "Meenu R",
        "profession": "UI/UX Designer",
        "skills": ["Figma", "Photoshop", "Illustrator"],
        "projects": [
            {"name": "E-commerce Design", "status": "Completed"},
            {"name": "Portfolio Site", "status": "In Progress"}
        ]
    }
}

@app.route('/')
def home():
    return "<h2>Welcome to the Static Portfolio Generator</h2><p>Try /portfolio/ragul</p>"

@app.route('/portfolio/<name>')
def profile(name):
    data = profiles.get(name.lower())
    if not data:
        return "<h3>Profile not found!</h3>"

    return f"""
    <h1>{data['name']}</h1>
    <p><b>Profession:</b> {data['profession']}</p>
    <p><a href='/portfolio/{name}/skills'>Skills</a> | 
       <a href='/portfolio/{name}/projects'>Projects</a></p>
    """

@app.route('/portfolio/<name>/skills')
def skills(name):
    data = profiles.get(name.lower())
    if not data:
        return "<h3>Skills not found for this user.</h3>"

    skills_list = "".join(f"<li>{skill}</li>" for skill in data['skills'])
    return f"""
    <h2>{data['name']}'s Skills</h2>
    <ul>{skills_list}</ul>
    <a href='/portfolio/{name}'>Back to profile</a>
    """

@app.route('/portfolio/<name>/projects')
def projects(name):
    data = profiles.get(name.lower())
    if not data:
        return "<h3>Projects not found for this user.</h3>"

    project_table = "<table border='1'><tr><th>Project</th><th>Status</th></tr>"
    for proj in data['projects']:
        project_table += f"<tr><td>{proj['name']}</td><td>{proj['status']}</td></tr>"
    project_table += "</table>"

    return f"""
    <h2>{data['name']}'s Projects</h2>
    {project_table}
    <br><a href='/portfolio/{name}'>Back to profile</a>
    """

if __name__ == '__main__':
    app.run(debug=True)
