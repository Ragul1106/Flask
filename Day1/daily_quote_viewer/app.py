from flask import Flask
import datetime

app = Flask(__name__)

quotes = {
    "monday": "Start your week with purpose.",
    "tuesday": "Keep going, you're doing great!",
    "wednesday": "Halfway there, stay strong!",
    "thursday": "Push forward with confidence.",
    "friday": "Celebrate your wins today!",
    "saturday": "Relax and recharge.",
    "sunday": "Plan and prepare for greatness."
}

@app.route('/')
def today_quote():
    today = datetime.datetime.now().strftime('%A').lower()
    quote = quotes.get(today, "Stay inspired!")
    return f"""
        <div style="font-family: Arial; text-align: center; margin-top: 100px;">
            <h1 style="color: #4CAF50;">Quote for Today ({today.title()})</h1>
            <p style="font-size: 24px;">"{quote}"</p>
        </div>
    """

@app.route('/quote/<day>')
def quote_by_day(day):
    day = day.lower()
    quote = quotes.get(day)
    if quote:
        return f"""
            <div style="font-family: Arial; text-align: center; margin-top: 100px;">
                <h1 style="color: #2196F3;">Quote for {day.title()}</h1>
                <p style="font-size: 24px;">"{quote}"</p>
            </div>
        """
    else:
        return f"""
            <div style="font-family: Arial; text-align: center; margin-top: 100px;">
                <h1 style="color: red;">Invalid Day!</h1>
                <p>Please enter a valid weekday (e.g., /quote/monday)</p>
            </div>
        """

if __name__ == '__main__':
    app.run(debug=True)
