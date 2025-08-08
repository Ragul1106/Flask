from flask import Flask, render_template_string, request, redirect, url_for

app = Flask(__name__)
votes = {}

@app.route('/poll', methods=['GET'])
def poll_form():
    return render_template_string("""
        <h2>Vote Now</h2>
        <form action="{{ url_for('vote') }}" method="POST">
            Name: <input type="text" name="name"><br>
            Option:
            <select name="option">
                <option value="A">A</option>
                <option value="B">B</option>
                <option value="C">C</option>
            </select><br>
            <button type="submit">Vote</button>
        </form>
    """)

@app.route('/vote', methods=['POST'])
def vote():
    name = request.form.get('name')
    option = request.form.get('option')
    votes[name] = option
    return redirect(url_for('result'))

@app.route('/result')
def result():
    option = request.args.get('option')
    if option:
        count = list(votes.values()).count(option)
        return {"option": option, "count": count}
    return {"votes": votes}

@app.route('/voter/<name>')
def voter(name):
    return {"name": name, "vote": votes.get(name)}

if __name__ == '__main__':
    app.run(debug=True)