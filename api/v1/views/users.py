#!/usr/bin/python3
from flask import jsonify, request, abort
from api.v1.views import app_views
from models.user import User
from models import storage

@app_views.route("/users", methods=["GET"], strict_slashes=False)
def get_users():
    """Get all users"""
    users  = [user.to_dict() for user in storage.all(User).values()]
    for user in users:
        del user['password']
    return jsonify(users)


@app_views.route("/users/<user_id>", methods=["GET"], strict_slashes=False)
def get_user(user_id):
    """Get a user"""
    user = storage.get(User, user_id)
    if user is None:
        abort(404)
    return jsonify(user.to_dict())


@app_views.route("/users/<user_id>", methods=["PUT"], strict_slashes=False)
def update_user(user_id):
    """Update a user"""
    user = storage.get(User, user_id)
    if not user:
        abort(404)
    data = request.get_json()
    if not data:
        abort(400, description="Not a JSON")
    
    # authenticate user here
    
    ignore = ["id", "email", "created_at", "updatd_at"]

    for key, val in data.items():
        if key not in ignore:
            setattr(user, key, val)
    storage.save()
    return jsonify(user.to_dict()), 200


@app_views.route("/users", methods=["POST"])
def post_user():
    """Creates a new user"""
    data = request.get_json()
    if not data:
        abort(400, description="Not a JSON")
    
    if "email" not in data:
        abort(400, description="Missing email")
    if "password" not in data:
        abort(400, description="Missing password")

    new_user = User(**data)
    new_user.save()
    return jsonify(new_user.to_dict()), 201
