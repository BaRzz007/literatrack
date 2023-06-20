#!/usr/bin/python3
"""Author module"""
from models.base_model import BaseModel


class Author(BaseModel):
    """Author class"""
    name = ""

    @property
    def books(self):
        """All books by author"""
        from models.book import Book
        from models import storage
        return [book for book in storage.all(Book).values()
                if self.id in book.author_ids]
    