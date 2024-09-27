#!/usr/bin/python3
"""
Module handles all endpoints for reviews
"""
from models import storage
from models.user import User
from models.review import Review
from flask import jsonify, request
from api.v1.views import app_views


@app_views.route("/users/<user_id>/reviews", methods=["GET", "POST"],
        strict_slashes=False)
def get_post_reviews():
    """
    GET: Returns all reviews made by the user
    POST: Creates a new review about a book
    """
    user = storage.get(User, data["user_id"])
    if not user:
        return jsonify({"error": "user not found"}), 404

    if request.method == "GET":
        reviews = [review.to_dict() for review in storage.all(Review)
                if review.user_id == review.id]
        return jsonify(reviews)

    if request.method == "POST":
        if not request.get_json():
            return jsonify({"error": "not a JSON"}), 400

        data = request.get_json()

        if "review" not in data:
            return jsonify({"error": "review is missing"}), 400

        if "book_id" not in data:
            return jsonify({"error": "user_id is missing"}), 400

        review = Review()
        review.user_id = data["user_id"]
        review.book_id = data["book_id"]
        review.save()
        return jsonify(review.to_dict()), 201

@app_views.route("/reviews/<review_id>", methods=["GET", "PUT"],
        strict_slashes=False)
def get_put_reviews(review_id):
    """
    GET: Returns a review
    PUT: updates a review
    """
    review = storage.get(Review, review_id)
    if not review:
        return jsonify({"error": "review not found"}), 404

    if request.method == "GET":
        return jsonify(review.to_dict()), 200

    if request.method == "PUT":
        if not request.get_json():
            return jsonify({"error": "not a JSON"}), 404

        data = request.get_json()

        if "user_id" not in data:
            return jsonify({"error": "user_id is missing"}), 400

        user = storage.get(User, data["user_id"])
        if not user:
            return jsonify({"error": "user not found"}), 404

        if "review" not in data:
            return jsonify({"error": "review is missing"}), 400

        review.review = data["review"]

        return jsonify(review.to_dict()), 200
