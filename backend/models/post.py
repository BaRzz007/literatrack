#!/usr/bin/python3
"""this file defines the post class"""
from models.base_model import BaseModel
from sqlalchemy.orm import Mapped, mapped_column
import datetime


class Post():
    """post class"""
    __tablename__ = 'posts'
    post: Mapped[str]
    post_date: Mapped[datetime.datetime]
