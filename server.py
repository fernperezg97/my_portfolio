import os
from flask import Flask, render_template, redirect, flash

app = Flask(__name__)
app.secret_key = os.environ.get('PORTFOLIO_FLASK_SECRET_KEY')
app.config['PRESERVE_CONTEXT_ON_EXCEPTION'] = True


@app.route("/")
def home():
    """return homepage"""

    return render_template("home.html")


@app.route("/portfolio")
def portfolio():
    """return portfolio"""

    return render_template("portfolio.html")


@app.route("/about")
def about_me():
    """return about me"""

    return render_template("about.html")


@app.route("/contact")
def contact():
    """return contact"""

    return render_template("contact.html")


@app.route("/blog")
def blog():
    """return blog"""

    return render_template("blog.html")














if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)