#!/usr/bin/env python3
"""Flask app"""
from models import storage
from flask import Flask, jsonify, make_response
from flask_cors import CORS
from api.v2.views import app_views

app = Flask(__name__)
#todo: understand why we used this config
app.config["JSONIFY_PRETTYPRINT_REGULAR"] = True
#todo: understand the use of blueprints
app.register_blueprint(app_views)
#todo: understand cors
cors = CORS(app, resources={r"api/v2/*": {"origins": "*"}})


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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, threaded=True, debug=True)
