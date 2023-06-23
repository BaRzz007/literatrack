#!/usr/bin/python3
"""shelf module"""
from models.base_model import BaseModel


class Shelf(BaseModel):
    """Shelf class"""
    user_id = ""
    name = ""
    book_ids = []

    @property
    def books(self):
        """Returns all books in shelf"""
        from models import storage
        self.book_ids = [shelf_books.book_id
                         for shelf_books in storage.all(ShelfBook).values()
                         if shelf_books.shelf_id == self.id]
        return self.book_ids
    
    @books.setter
    def books(self, book):
        """append book to shelf"""
        from models.book import Book
        from models import storage
        if isinstance(book, Book) and \
            book in storage.all(Book) and \
                not storage.all(ShelfBook).get(f"ShelfBook.{self.id}.{book.id}"):
            temp = ShelfBook(**{"book_id": book.id, "shelf_id": self.id})
            temp.save()
            self.book_ids.append(book.id)


class ShelfBook(BaseModel):
    """ShelfBook lookup class"""

    def __init__(self, *args, **kw):
        """Initialization"""
        self.id = f"{kw['shelf_id']}.{kw['book_id']}"
        self.shelf_id = kw["shelf_id"]
        self.book_id = kw["book_id"]
        
