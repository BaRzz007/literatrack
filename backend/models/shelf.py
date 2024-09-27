#!/usr/bin/python3
"""shelf module"""
from models.base_model import BaseModel


class Shelf(BaseModel):
    """Shelf class"""
    user_id = ""
    name = ""
    book_count = 0
    book_ids = []

    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not kwargs:
            self.book_ids = []
    
    @property
    def books(self):
        """Returns all books in shelf"""
        from models import storage
        from models.book import Book
        book_ids_list = [
                book.id for book in storage.all(Book).values()
                if book.id in self.book_ids]
        # self.book_count = len(self.book_ids)
        return book_ids_list
    """ 
    @books.setter
    def books(self, book):
        
        append book to shelf
        
        from models.book import Book
        from models import storage
        if isinstance(book, Book) and book in storage.all(Book).values() and \
                book.id not in self.book_ids:
                    self.book_ids += [book.id]
                    self.book_count += 1
    """
