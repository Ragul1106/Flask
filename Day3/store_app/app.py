from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html", title="Home")

@app.route("/products")
def products():
    products_list = [
        {
            "name": "Laptop Pro 15",
            "price": 1299.99,
            "in_stock": True,
            "image": "laptop.jpeg"
        },
        {
            "name": "Smartphone X",
            "price": 899.50,
            "in_stock": False,
            "image": "phone.jpeg"
        },
        {
            "name": "Wireless Headphones",
            "price": 199.99,
            "in_stock": True,
            "image": "headphone.jpeg"
        }
    ]
    return render_template("products.html", title="Products", products=products_list)

if __name__ == "__main__":
    app.run(debug=True)
