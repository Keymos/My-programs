# save this as app.py
# Understanding how to build a web app

from flask import Flask, render_template, url_for


app = Flask(__name__)

posts = [
    {
    "author": "Mimsy",
    "title": "Blog Post 1",
    "content": "First blog post content",
    "date_posted": "April 20, 2023"
    },
    {
    "author": "Emma",
    "title": "Blog Post 2",
    "content": "Second blog post content",
    "date_posted": "April 21, 2023"
    }
]


@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html", posts=posts)

@app.route('/about')
def about():
    return render_template("about.html", title="About")


if __name__ == '__main__':
    app.run(debug=True)