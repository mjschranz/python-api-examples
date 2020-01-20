from flask import Flask, render_template, url_for

app = Flask(__name__)

posts = [
    {
        "author": "Matthew Schranz",
        "title": "Blog Post 1",
        "content": "First blog post content",
        "date_posted": "January 19, 2020",
    },
    {
        "author": "Karen Schranz",
        "title": "Blog Post 2",
        "content": "Second blog post content",
        "date_posted": "January 20, 2020",
    },
]


@app.route("/")
@app.route("/home")
def index_page():
    return render_template("home.html", posts=posts)


@app.route("/about")
def about_page():
    return render_template("about.html", title="About Page")


if __name__ == "__main__":
    app.run(debug=True)

