#!/usr/bin/python3
from flask import jsonify, request
from models import storage
from models.book import Book
from api.v1.views import app_views
import requests


@app_views.route("/books", methods=["GET"], strict_slashes=False)
def get_books():
    """Get all books in my storage"""
    books = [book.to_dict() for book in storage.all(Book).values()]
    return jsonify(books)


@app_views.route("/book_search", methods=["GET"], strict_slashes=False)
def search_books():
    """Search books by title"""
    search_keyword = request.args.get("q")
    page = request.args.get("page")
    if page.isdigit():
        page = int(page)

    max_val = 40

    if page is None or page <= 0:
        page = 1
    if page == 1:
        start_idx = 0
    else:
        start_idx = page * max_val + 1
    url = "https://www.googleapis.com/books/v1/volumes?"
    resp = requests.get(
        f"{url}q={search_keyword}&startIndex={start_idx}&maxResult={max_val}")
    books = resp.json()
    return jsonify(books)
