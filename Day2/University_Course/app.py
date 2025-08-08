from flask import Flask, render_template_string, request, redirect, url_for

app = Flask(__name__)

courses = [
    {"code": "CS101", "name": "Intro to Computer Science", "dept": "CS"},
    {"code": "CS102", "name": "Data Structures", "dept": "CS"},
    {"code": "MATH201", "name": "Calculus", "dept": "Math"}
]
registrations = []

@app.route('/courses')
def course_list():
    dept = request.args.get('dept')
    if dept:
        filtered = [c for c in courses if c['dept'].lower() == dept.lower()]
        return {"courses": filtered}
    return {"courses": courses}

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form.get('name')
        course_code = request.form.get('course_code')
        registrations.append({"name": name, "course_code": course_code})
        return redirect(url_for('confirm_registration', name=name))
    return render_template_string("""
        <h2>Register for a Course</h2>
        <form method="POST">
            Student Name: <input type="text" name="name"><br>
            Course Code: <input type="text" name="course_code"><br>
            <button type="submit">Register</button>
        </form>
    """)

@app.route('/confirm-registration/<name>')
def confirm_registration(name):
    return f"<h2>Registration successful for {name}!</h2>"


if __name__ == '__main__':
    app.run(debug=True)