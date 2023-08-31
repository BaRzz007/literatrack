#!/usr/bin/python3
"""
This module contains all endpoints that 
handles all associations between a shelf and a book
"""
from models import storage
from models.shelf import Shelf
from models.book import Book
from flask import jsonify, request
from api.v1.views import app_views


@app_views.route("/shelfs/<shelf_id>/books", methods=["GET"],
        strict_slashes=False)
def get_shelf_books(shelf_id):
    """
    GET: Returns all books in a user's shelf
    """
    shelf = storage.get(Shelf, shelf_id)
    if not shelf:
        return jsonify({"error": "shelf not found"}), 404

    books = [book.to_dict() for book in storage.all(Book).values()
            if book.id in shelf.books]

    return jsonify(books), 200


@app_views.route("/shelfs/<shelf_id>/books/<book_id>", methods=["POST", "DELETE"],
        strict_slashes=False)
def post_delete_shelfs_books(shelf_id, book_id):
    """
    POST: Associates a book with a shelf
    DELETE: Removes a book from a shelf
    """
    shelf = storage.get(Shelf, shelf_id)
    if not shelf:
        return jsonify({"error": "shelf not found"}), 404

    book = storage.get(Book, book_id)
    if not book:
        return jsonify({"error": "book not found"}), 404

    if request.method == "POST":
        if book_id not in shelf.books:
            # possibly going to refactor this code to be clearer if time permits
            # code should read: shelf.book_ids.append(book)
            shelf.book_ids.append(book.id)
            shelf.book_count = len(shelf.books)
            storage.save()
            return jsonify(shelf.to_dict()), 201
        return jsonify(shelf.to_dict()), 200

    if request.method == "DELETE":
        if book_id not in shelf.book_ids:
            return jsonify({"error": "book not found in shelf"}), 404
        shelf.book_ids.remove(book_id)
        shelf.book_count = len(shelf.books)
        storage.save()
        return jsonify({}), 200
