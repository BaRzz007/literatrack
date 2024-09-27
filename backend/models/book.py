#!/usr/bin/python3
"""book module"""
from models.base_model import BaseModel


class Book(BaseModel):
    """Book class"""
    title = ""
    isbn = ""
    published_date = ""
    publisher = ""
    description = ""
    page_count = 0
