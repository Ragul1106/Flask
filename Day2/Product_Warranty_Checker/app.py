from flask import Flask, render_template_string, request, redirect, url_for

app = Flask(__name__)

warranty_data = {
    "ABC123": "Valid until 2026-12-31",
    "XYZ789": "Expired",
    "LMN456": "Valid until 2027-05-15"
}

@app.route('/check-warranty', methods=['GET', 'POST'])
def check_warranty():
    if request.method == 'POST':
        serial = request.form.get('serial')
        return redirect(url_for('warranty_result', serial=serial))
    return render_template_string("""
        <h2>Check Product Warranty</h2>
        <form method="POST">
            Serial Number: <input type="text" name="serial"><br>
            <button type="submit">Check</button>
        </form>
    """)

@app.route('/result')
def warranty_result():
    serial = request.args.get('serial')
    result = warranty_data.get(serial, "Not found")
    return {"serial": serial, "warranty": result}

@app.route('/warranty/<product>')
def warranty_product(product):
    result = warranty_data.get(product, "Not found")
    return {"product": product, "warranty": result}

if __name__ == '__main__':
    app.run(debug=True)