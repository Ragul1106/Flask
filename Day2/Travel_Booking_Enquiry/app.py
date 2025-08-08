from flask import Flask, render_template_string, request, redirect, url_for

app = Flask(__name__)


bookings = []
travel_deals = [
    {"destination": "paris", "deal": "20% off flights"},
    {"destination": "london", "deal": "Free hotel night"},
    {"destination": "tokyo", "deal": "Discount on tours"},
]

@app.route('/booking', methods=['GET', 'POST'])
def booking():
    if request.method == 'POST':
        name = request.form.get('name')
        destination = request.form.get('destination')
        travel_date = request.form.get('travel_date')
        bookings.append({"name": name, "destination": destination, "travel_date": travel_date})
        return redirect(url_for('booking_confirm', name=name))
    return render_template_string("""
        <h2>Travel Booking</h2>
        <form method="POST">
            Name: <input type="text" name="name"><br>
            Destination: <input type="text" name="destination"><br>
            Travel Date: <input type="date" name="travel_date"><br>
            <button type="submit">Book</button>
        </form>
    """)

@app.route('/booking/confirm/<name>')
def booking_confirm(name):
    return f"<h2>Booking confirmed for {name}!</h2>"

@app.route('/deals')
def deals():
    destination = request.args.get('destination')
    if destination:
        filtered = [d for d in travel_deals if d['destination'].lower() == destination.lower()]
        return {"deals": filtered}
    return {"deals": travel_deals}

if __name__ == '__main__':
    app.run(debug=True)