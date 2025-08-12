from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html", title="Home")

@app.route("/blogs")
def blogs():
    blog_list = [
        {
            "title": "The Art of Cooking",
            "author": "Ragul R",
            "snippet": "Discover the magic of creating delicious meals at home...",
            "image": "blog1.png",
            "featured": True
        },
        {
            "title": "Travel Guide: Japan",
            "author": "Libi N",
            "snippet": "From Tokyo's bustling streets to Kyoto's peaceful temples...",
            "image": "blog2.jpeg",
            "featured": False
        },
        {
            "title": "Mindfulness in Daily Life",
            "author": "Heera R",
            "snippet": "Practical tips to stay present and live with intention...",
            "image": "blog3.jpeg",
            "featured": True
        }
    ]
    return render_template("blogs.html", blogs=blog_list)

if __name__ == "__main__":
    app.run(debug=True)
