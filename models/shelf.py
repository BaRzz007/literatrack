#!/usr/bin/python3
"""shelf module"""
from models.base_model import BaseModel


class Shelf(BaseModel):
    """Shelf class"""
    user_id = ""
    name = ""
    book_count = 0
    book_ids = []

    @property
    def books(self):
        """Returns all books in shelf"""
        return self.book_ids
    
    @books.setter
    def books(self, book):
        """append book to shelf"""
        from models.book import Book
        from models import storage
        if isinstance(book, Book) and book in storage.all(Book).values() and \
                book.id not in self.book_ids:
                    self.book_ids.append(book.id)
                    self.book_count += 1
