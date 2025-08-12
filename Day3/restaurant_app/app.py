from flask import Flask, render_template

app = Flask(__name__)

@app.route("/menu")
def menu():
    menu_data = {
        "Starter": [
            {"name": "Tomato Soup", "price": 150, "available": True, "image": "starter1.jpeg"},
            {"name": "Garlic Bread", "price": 100, "available": False, "image": "starter2.jpeg"}
        ],
        "Main": [
            {"name": "Grilled Chicken", "price": 350, "available": True, "image": "main1.jpeg"},
            {"name": "Paneer Butter Masala", "price": 300, "available": True, "image": "main2.jpeg"}
        ],
        "Dessert": [
            {"name": "Chocolate Cake", "price": 200, "available": False, "image": "dessert1.jpeg"},
            {"name": "Ice Cream", "price": 120, "available": True, "image": "dessert2.jpeg"}
        ]
    }
    return render_template("menu.html", menu_data=menu_data)

if __name__ == "__main__":
    app.run(debug=True)
