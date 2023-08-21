#!/usr/bin/python3
"""review module"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Review class"""
    user_id = ""
    book_id = ""
    review = ""
