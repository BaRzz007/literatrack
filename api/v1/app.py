#!/usr/bin/python3
"""Flask app"""
from models import storage
from flask import Flask, jsonify, make_response
#from flask_cors import CORS
from api.v1.views import app_views

app = Flask(__name__)
app.config["JSONIFY_PRETTYPRINT_REGULAR"] = True
app.register_blueprint(app_views)
#cors = CORS(app, resources={r"api/v1/*": {"origins": "*"}})


@app.teardown_appcontext
def close_db(error):
    """Close storage"""
    storage.close()


@app.errorhandler(404)
def not_found(error):
    """404 Error"""
    return make_response(jsonify({"error": "Not found"}), 404)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, threaded=True)
