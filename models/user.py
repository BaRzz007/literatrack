#!/usr/bin/python3
"""user module"""
from models.base_model import BaseModel


class User(BaseModel):
    """User class"""
    email = ""
    username = ""
    password = ""
    firstname = ""
    lastname = ""
