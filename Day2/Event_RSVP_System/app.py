from flask import Flask, render_template_string, request, redirect, url_for

app = Flask(__name__)

guests = []

@app.route('/rsvp', methods=['GET'])
def rsvp_form():
    return render_template_string("""
        <h2>RSVP</h2>
        <form action="{{ url_for('rsvp_confirm') }}" method="POST">
            Name: <input type="text" name="name"><br>
            Email: <input type="email" name="email"><br>
            Attending (yes/no): <input type="text" name="attending"><br>
            <button type="submit">Submit RSVP</button>
        </form>
    """)

@app.route('/rsvp-confirm', methods=['POST'])
def rsvp_confirm():
    name = request.form.get('name')
    email = request.form.get('email')
    attending = request.form.get('attending')
    guests.append({"name": name, "email": email, "attending": attending})
    return redirect(url_for('thank_guest', name=name))

@app.route('/thank-you/<name>')
def thank_guest(name):
    return f"<h2>Thank you for your RSVP, {name}!</h2>"

@app.route('/guests')
def list_guests():
    attending = request.args.get('attending')
    if attending:
        filtered = [g for g in guests if g['attending'].lower() == attending.lower()]
        return {"guests": filtered}
    return {"guests": guests}

if __name__ == '__main__':
    app.run(debug=True)
