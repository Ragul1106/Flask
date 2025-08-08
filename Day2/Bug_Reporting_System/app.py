from flask import Flask, render_template_string, request, redirect, url_for

app = Flask(__name__)

bugs = []

@app.route('/report', methods=['GET', 'POST'])
def report_bug():
    if request.method == 'POST':
        title = request.form.get('title')
        description = request.form.get('description')
        priority = request.form.get('priority')
        bug_id = len(bugs) + 1
        bugs.append({"id": bug_id, "title": title, "description": description, "priority": priority})
        return redirect(url_for('report_confirm'))
    return render_template_string("""
        <h2>Report a Bug</h2>
        <form method="POST">
            Title: <input type="text" name="title"><br>
            Description: <textarea name="description"></textarea><br>
            Priority: <input type="text" name="priority"><br>
            <button type="submit">Submit</button>
        </form>
    """)

@app.route('/report-confirm')
def report_confirm():
    return "<h2>Bug report submitted successfully!</h2>"

@app.route('/bugs')
def list_bugs():
    priority = request.args.get('priority')
    if priority:
        filtered = [b for b in bugs if b['priority'].lower() == priority.lower()]
        return {"bugs": filtered}
    return {"bugs": bugs}

@app.route('/bug/<int:id>')
def bug_details(id):
    bug = next((b for b in bugs if b['id'] == id), None)
    return bug if bug else {"error": "Bug not found"}

if __name__ == '__main__':
    app.run(debug=True)