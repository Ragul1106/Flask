from flask import Flask, render_template_string, request, redirect, url_for

app = Flask(__name__)

applications = []

@app.route('/apply', methods=['GET'])
def apply_form():
    return render_template_string("""
        <h2>Job Application</h2>
        <form action="{{ url_for('submit_application') }}" method="POST">
            Name: <input type="text" name="name"><br>
            Email: <input type="email" name="email"><br>
            Position: <input type="text" name="position"><br>
            <button type="submit">Apply</button>
        </form>
    """)

@app.route('/submit-application', methods=['POST'])
def submit_application():
    name = request.form.get('name')
    email = request.form.get('email')
    position = request.form.get('position')
    applications.append({"name": name, "email": email, "position": position})
    return redirect(url_for('application_status'))

@app.route('/application-status')
def application_status():
    return "<h2>Your application has been submitted!</h2>"

@app.route('/applications')
def list_applications():
    position = request.args.get('position')
    if position:
        filtered = [app for app in applications if app['position'] == position]
        return {"applications": filtered}
    return {"applications": applications}

@app.route('/applicant/<name>')
def applicant(name):
    data = [app for app in applications if app['name'] == name]
    return {"applicant": data}

if __name__ == '__main__':
    app.run(debug=True)