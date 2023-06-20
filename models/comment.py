#!/usr/bin/python3
"""comment module"""
from models.base_model import BaseModel


class Comment(BaseModel):
    """Comment class"""
    user_id = ""
    review_id = ""
    text = ""
    