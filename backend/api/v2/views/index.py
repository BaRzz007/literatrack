#!/usr/bin/env python3
"""Index"""
from flask import jsonify
from models import storage
from models.user import User
from models.book import Book
from models.category import Category
from models.collection import Collection
from models.author import Author
from models.note import Note
from models.post import Post
from models.comment import Comment
from models.publisher import Publisher
from models.reading_session import ReadingSession
from api.v2.views import app_views

@app_views.route("/status", methods=["GET"], strict_slashes=False)
def status():
    """Status of API"""
    return jsonify({"status": "OK"})

@app_views.route("/", methods=["GET"], strict_slashes=False)
def index():
    """count of models"""
    return jsonify({
        "Users": len(storage.all(User)),
        "Books": len(storage.all(Book)),
        "Categories": len(storage.all(Category)),
        "Collections": len(storage.all(Collection)),
        "Authors": len(storage.all(Author)),
        "Notes": len(storage.all(Note)),
        "Comments": len(storage.all(Comment)),
        "Publishers": len(storage.all(Publisher)),
        "Reading Sessions": len(storage.all(ReadingSession))
        })
