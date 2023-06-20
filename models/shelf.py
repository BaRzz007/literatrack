#!/usr/bin/python3
"""shelf module"""
from models.base_model import BaseModel


class Shelf(BaseModel):
    """Shelf class"""
    user_id = ""
    to_read = []
    reading = []
    done_read = []
    