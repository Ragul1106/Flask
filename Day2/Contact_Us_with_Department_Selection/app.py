from flask import Flask, request, redirect, url_for, render_template_string, flash

app = Flask(__name__)
contacts = []

@app.route('/contact', methods=['GET'])
def contact_form():
    return render_template_string("""
        <h2>Contact Us</h2>
        <form action="{{ url_for('submit_contact') }}" method="POST">
            Name: <input type="text" name="name"><br>
            Email: <input type="email" name="email"><br>
            Message: <textarea name="message"></textarea><br>
            Department: <input type="text" name="department"><br>
            <button type="submit">Send</button>
        </form>
    """)

@app.route('/submit', methods=['POST'])
def submit_contact():
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')
    department = request.form.get('department')
    source = request.args.get('source')
    contacts.append({"name": name, "email": email, "message": message,
                     "department": department, "source": source})
    flash("Your message has been sent successfully!")
    return redirect(url_for('contact_thank_you'))

@app.route('/contact/thank-you')
def contact_thank_you():
    return "<h2>Thank you for contacting us!</h2>"

@app.route('/contact/<department>')
def contact_department(department):
    dept_contacts = [c for c in contacts if c['department'] == department]
    return {"department": department, "contacts": dept_contacts}


if __name__ == '__main__':
    app.run(debug=True)