from flask import Flask, request, redirect, url_for

app = Flask(__name__)

mood_logs = []

@app.route("/log-mood", methods=["GET"])
def log_mood_form():
    return """
    <h2>Daily Mood Logger</h2>
    <form action="/mood-result" method="POST">
        <label>Name:</label><br>
        <input type="text" name="name" required><br><br>
        
        <label>Mood:</label><br>
        <select name="mood" required>
            <option value="happy">Happy</option>
            <option value="sad">Sad</option>
            <option value="excited">Excited</option>
            <option value="tired">Tired</option>
        </select><br><br>
        
        <label>Reason:</label><br>
        <textarea name="reason" required></textarea><br><br>
        
        <button type="submit">Submit</button>
    </form>
    """

@app.route("/mood-result", methods=["POST"])
def mood_result():
    name = request.form.get("name")
    mood = request.form.get("mood")
    reason = request.form.get("reason")

    mood_logs.append({"name": name, "mood": mood, "reason": reason})
    return redirect(url_for("thank_you", name=name))

@app.route("/logs")
def logs():
    mood_filter = request.args.get("mood")
    if mood_filter:
        filtered_logs = [log for log in mood_logs if log["mood"].lower() == mood_filter.lower()]
        if not filtered_logs:
            return f"<h3>No logs found for mood: {mood_filter}</h3>"
        result = "<h2>Filtered Mood Logs</h2>"
        for log in filtered_logs:
            result += f"<p><b>{log['name']}</b> - {log['mood']} ({log['reason']})</p>"
        return result
    else:
        if not mood_logs:
            return "<h3>No mood logs yet.</h3>"
        result = "<h2>All Mood Logs</h2>"
        for log in mood_logs:
            result += f"<p><b>{log['name']}</b> - {log['mood']} ({log['reason']})</p>"
        return result

@app.route("/thank-you/<name>")
def thank_you(name):
    return f"<h2>Thank you, {name}! Your mood has been recorded. ❤️</h2>"

if __name__ == "__main__":
    app.run(debug=True)
