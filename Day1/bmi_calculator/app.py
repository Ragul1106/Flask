from flask import Flask

app = Flask(__name__)

@app.route('/')
def usage():
    return """
    <h2>BMI Calculator</h2>
    <p>Use this format to calculate your BMI:</p>
    <p><b>/bmi/&lt;weight&gt;/&lt;height&gt;</b> (weight in kg, height in meters)</p>
    <p>Example: <a href="/bmi/70/1.75">/bmi/70/1.75</a></p>
    """

@app.route('/bmi/<float:weight>/<float:height>')
def calculate_bmi(weight, height):
    if height <= 0:
        return "Height must be greater than 0."

    bmi = round(weight / (height ** 2), 2)

    if bmi < 18.5:
        category = "Underweight"
    elif 18.5 <= bmi < 24.9:
        category = "Normal weight"
    elif 25 <= bmi < 29.9:
        category = "Overweight"
    else:
        category = "Obese"

    return f"""
    <h1>Your BMI Result</h1>
    <p><b>BMI:</b> {bmi}</p>
    <p><b>Category:</b> {category}</p>
    <hr>
    <p>Stay healthy and eat well!</p>
    """

if __name__ == '__main__':
    app.run(debug=True)
