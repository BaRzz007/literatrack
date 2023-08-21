#!/usr/bin/python3
from flask import jsonify, request, abort
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
    """Search books by search keyword"""
    search_keyword = request.args.get("q", default="")
    search_term = request.args.get("term", default="")
    page = request.args.get("page", default=1, type=int)
    # if page.isdigit():
    #    page = int(page)
    max_val = 40

    if page <= 0:
        page = 1

    start_idx = 0
    if page > 1:
        start_idx = (page - 1) * max_val + 1

    url = "https://www.googleapis.com/books/v1/volumes?"
    resp = requests.get(
        f"{url}q={search_keyword}&startIndex={start_idx}&maxResults={max_val}")
    books_dict_list = resp.json()
    
    books = []
    for book_dict in books_dict_list:
        book = {}
        book["title"] = book_dict["volumeInfo"]["title"]
        if book_dict["industryIdentifiers"][0]["type"] == "ISBN_13":
            book["isbn"] = book_dict["industryIdentifiers"][0]["identifier"]
        else:
            book["isbn"] = book_dict["industryIdentifiers"][1]["identifier"]
        
        # datetime.strptime(book_dict["publishedDate"], "%Y-%m-%d")
        book["published_date"] = book_dict["publishedDate"]
        book["publisher"] = book_dict["publisher"]
        book["description"] = book_dict["description"]
        book["authors"] = book_dict["volumeInfo"]["authors"]
        book["page_count"] = book_dict["pageCount"]
        books.append(book)
    return jsonify(books)


@app_views.route("/books", methods=["POST"], strict_slashes=False)
def post_book():
    """Create a new book and add to database"""
    if not request.get_json():
        abort(400, description="Not a JSON")
    if "isbn" not in request.get_json():
        abort(400, description="Missing ISBN")
    if "user_id" not in request.get_json():
        abort(400, descripton="Missing user_id")
    book = request.get_json()
    book_json = request.get(f"https://www.googleapis.com/books/v1/volumes?q={book['isbn']}")
    all_books = storage.all(Book)
    if len([book for book in storage.all(Book).values() if book.ISBN == book_json["isbn"]]) == 0:
        new_book = Book()
        return jsonify(new_book)
