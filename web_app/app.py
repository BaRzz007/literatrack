#!/usr/bin/python3
from flask import Flask, render_template
from models import storage
from models.user import User

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    """Index page"""
    users = list(storage.all(User).values())
    user = users[0]
    return render_template("index.html", user=user)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)