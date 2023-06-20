#!/usr/bin/python3
"""review module"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Review class"""
    user_id = ""
    book_id = ""
    text = ""
    page_num = 0
    type = ""
    like_count = 0
    