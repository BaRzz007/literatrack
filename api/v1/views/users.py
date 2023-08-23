#!/usr/bin/python3
from flask import flask, jsonify, request, abort
from api.vi.views import app_views
from models.user import User
from models import storage


@app_views.route("/users", methods=["GET", "POST"], strict_slashes=False)
def get_post_users():
    """
    GET: Retrieves the list of all users
    POST: Adds a user
    """

    if request.method == "POST":
        if not request.get_json():
            abort(400, description="Not a JSON")
        if "email" not in request.get_json():
            abort(400, description="Missing email")
        if "password" not in request.get_json():
            abort(404, description="Missing password")


        data = request.get_json()
        instance = User(**data)
        instance.save()
        return jsonify(instance.to_dict()), 201

    if request.method == "GET":
        all_users = storage.all(User).values()
        list_users = [user.dict() for user in all_users]
        return jsonify(list_users)

@app_views.route("/users/<user_id>", methods=["GET", "PUT", "DELETE"], strict_slashes=False)
def get_update_user(user_id):
    """
    GET: Retrieves a user by id
    PUT: Updates a user
    DELETE: Deletes a user
    """
    user = storage.get(user, user_id)
    if not user:
        abort(404)

    if request.method == "GET":
        return jsonify(user.to_dict), 200

    if request.method == "PUT":
        if not request.get_json():
            return(400, description="Not a JSON")

        ignore_list = ["id", "email", "created_at", "updated_at"]

        data = request.get_json()
        for key, value in data:
            if not in ignore_list:
                setattr(user, key, value)
        user.save()
        return jsonify(user.to_dict()), 200

    if request.method == "DELETE":
        user.delete()
        return jsonify({}), 200
