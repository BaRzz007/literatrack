#!/usr/bin/python3
"""
Shelf API module
"""
from api.v1.views import app_views
from flask import abort, jsonify, request
from models import storage
from models.shelf import Shelf
from models.user import User


@app_views.route("/users/<user_id>/shelfs",
        methods=["POST", "GET"], strict_slashes=False)
def post_get_user_shelfs(user_id):
    """
    POST: Add a shelf to user library
    GET: Retrieve all user shelf
    """
    user = storage.get(User, user_id)
    if not user:
        return jsonify({"error": "user not found"}), 404

    if request.method == "POST":
        if not request.get_json():
            return jsonify({"error": "Not a JSON"}), 400

        if "name" not in request.get_json():
            return jsonify({"error": "name is missing"}), 400

        data = request.get_json()
        shelf = Shelf()
        shelf.name = data["name"]
        shelf.user_id = user_id
        shelf.save()
        return jsonify(shelf.to_dict()), 201

    if request.method == "GET":
        shelf_list = [shelf for shelf in storage.all(Shelf).values()]
        user_shelf_list = [shelf.to_dict() for shelf in shelf_list
                if shelf.user_id == user_id]
        return jsonify(user_shelf_list), 200


@app_views.route("/shelfs/<shelf_id>", methods=["GET", "PUT", "DELETE"],
        strict_slashes=False)
def get_put_delete_shelf(shelf_id):
    """
    GET: Returns a shelf resource
    PUT: Updates a shelf resource
    DELETE: Deletes a shelf
    """
    shelf = storage.get(Shelf, shelf_id)
    if not shelf:
        return jsonify({"error": "not a JSON"}), 400

    if request.method == "GET":
        return jsonify(shelf.to_dict()), 200

    if request.method == "PUT":
        if not request.get_json():
            return jsonify({"error": "not a JSON"}), 400

        data = request.get_json()

        ignore = ["id", "created_at", "updated_at", "user_id"]
        for key, value in data.items():
            if key not in ignore:
                setattr(shelf, key, value)
        shelf.save()
        return jsonify(shelf.to_dict()), 200

    if request.method == "DELETE":
        shelf.delete()
        return jsonify({}), 200
