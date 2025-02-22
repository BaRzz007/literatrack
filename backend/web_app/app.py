#!/usr/bin/python3
from flask import Flask, render_template, jsonify, make_response
from flask_cors import CORS
from models import storage
from models.user import User
from api.v1.views import app_views

app = Flask(__name__)
app.config["JSONIFY_PRETTYPRINT_REGULAR"] = True
app.register_blueprint(app_views)
cors = CORS(app, resources={r"api/v1/*": {"origins": "*"}})


@app.teardown_appcontext
def close_db(error):
    """Close storage"""
    storage.close()


@app.errorhandler(404)
def not_found(error):
    """404 Error"""
    return make_response(jsonify({"error": "Not found"}), 404)

@app.errorhandler(500)
def server_error(error):
    return make_response(jsonify({"error": "Something went wrong"}), 500)


@app.route("/", strict_slashes=False)
def index():
    """Index page"""
    return render_template("index.html")

@app.route("/login", strict_slashes=False)
def login():
    """Login specific things"""
    return "Log user in"

@app.route("/signup")
def signup():
    """Signup specific things"""
    return "Register user"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
