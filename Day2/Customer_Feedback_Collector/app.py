from flask import Flask, request, redirect, url_for, render_template_string

app = Flask(__name__)
feedback_list = []

@app.route('/feedback-form', methods=['GET'])
def feedback_form():
    return render_template_string("""
        <h2>Feedback Form</h2>
        <form action="{{ url_for('submit_feedback') }}" method="POST">
            Name: <input type="text" name="name"><br>
            Email: <input type="email" name="email"><br>
            Message: <textarea name="message"></textarea><br>
            <button type="submit">Submit</button>
        </form>
    """)

@app.route('/submit-feedback', methods=['POST'])
def submit_feedback():
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')
    feedback_list.append({"name": name, "email": email, "message": message})
    return redirect(url_for('thank_you'))

@app.route('/thank-you')
def thank_you():
    return "<h2>Thank you for your feedback!</h2>"

@app.route('/feedbacks')
def feedbacks():
    user = request.args.get('user')
    if user:
        filtered = [fb for fb in feedback_list if fb['name'] == user]
        return {"feedbacks": filtered}
    return {"feedbacks": feedback_list}

@app.route('/user/<username>')
def user_feedback(username):
    user_data = [fb for fb in feedback_list if fb['name'] == username]
    return {"user_feedback": user_data}

if __name__ == '__main__':
    app.run(debug=True)