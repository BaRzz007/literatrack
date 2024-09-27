#!/usr/bin/python3
""" """
from flask import jsonify, request
from api.v1.views import app_views
from models.user import User
from models.read_session import ReadSession
from models import storage


@app_views.route("/users/<user_id>/readsessions", methods=["GET", "POST"],
        strict_slashes=False)
def get_post_all_readsession(user_id):
    """
    GET: Returns all readsession of a user
    POST: Begins or adds a new session for a book in a user's shelf
    if none exists for that book prior
    """
    user = storage.get(User, user_id)
    if not user:
        return jsonify({"error": "user not found"}), 404

    sessions = [session.to_dict() for session in storage.all(ReadSession).values()
            if session.user_id == user.id]

    if request.method == "GET":
        return jsonify(sessions), 200

    if request.method == "POST":
        if not request.get_json():
            return jsonify({"error": "not a JSON"}), 400

        data = request.get_json()

        if "book_id" not in data:
            return jsonify({"error": "book_id is missing"}), 400
        for session in sessions:
            if session["book_id"] == data["book_id"]:
                return jsonify(session), 200
        new_session = ReadSession()
        new_session.book_id = data["book_id"]
        new_session.user_id = user_id
        new_session.save()
        return jsonify(new_session.to_dict()), 201


@app_views.route("/readsessions/<readsession_id>", methods=["GET", "POST"],
        strict_slashes=False)
def get_put_readsession(readsession_id):
    """
    GET: Returns a user's readsession associated with a book
    PUT: Updates a user's readsession
    """
    session = storage.get(ReadSession, readsession_id)
    if not session:
        return jsonify({"error": "session not found"}), 404

    if request.method == "GET":
        return jsonify(session.to_dict()), 200

    if request.method == "PUT":
        if not request.json():
            return jsonify({"error": "not a JSON"}), 400

        data = request.json()

        ignore = ["id", "created_at", "updated_at", "book_id"]
        for key, value in data.items():
            if key not in ignore:
                setattr(session, key, value)
        session.save()
        return jsonify(session.to_dict()), 200
