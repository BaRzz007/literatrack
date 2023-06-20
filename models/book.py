#!/usr/bin/python3
"""Book model module"""
from models.base_model import BaseModel



class Book(BaseModel):
    """Book class"""
    title = ""
    ISBN = ""
    publish_date = ""
    publisher = ""
    page_count = 0
    description = ""
    author_ids = []

    @property
    def authors(self):
        """All authors"""
        from models import storage
        self.author_ids = [book_author.author_id for book_author in storage.all(BookAuthor).values()
                           if book_author.book_id == self.id]
        return self.author_ids
    
    @authors.setter
    def authors(self, author):
        """Returns list of author IDs"""
        from models.author import Author
        from models import storage
        if isinstance(author, Author) and \
            author in storage.all(Author).values() and \
                not storage.all(BookAuthor).get(f"{BookAuthor.__name__}.{self.id}.{author.id}"):
            temp = BookAuthor(**{"book_id": self.id, "author_id": author.id})
            temp.save()
            self.author_ids.append(author.id)


class BookAuthor(BaseModel):
    """Lookup class"""
    
    def __init__(self, *args, **kw):
        """Initialization"""
        self.id = f"{kw['book_id']}.{kw['author_id']}"
        self.book_id = kw["book_id"]
        self.author_id = kw["author_id"]

