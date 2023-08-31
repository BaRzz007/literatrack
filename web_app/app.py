#!/usr/bin/python3
from flask import Flask, render_template
from models import storage
from models.user import User

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    """Index page"""
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
