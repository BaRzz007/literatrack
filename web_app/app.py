#!/usr/bin/python3
from flask import Flask, render_template
from models import storage
from models.review import Review
from models.user import User
from models.comment import Comment

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    """Index page"""
    reviews = list(storage.all(Review).values())
    users = list(storage.all(User).values())
    comments = list(storage.all(Comment).values())
    return render_template("index.html",
                           reviews=reviews,
                           users=users,
                           comments=comments)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)