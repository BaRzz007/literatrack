#!/usr/bin/env python3
"""this file defines the post class"""
from typing import List
from models.base_model import BaseModel
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
import datetime


class Post(BaseModel):
    """post class"""
    __tablename__ = 'posts'
    post: Mapped[str] = mapped_column(String(1000))
    privacy: Mapped[str] = mapped_column(String(20), default='public')
    user_id: Mapped[str] = mapped_column(ForeignKey('users.id', ondelete='CASCADE'))
    user: Mapped['User'] = relationship()
    book_id: Mapped[str] = mapped_column(ForeignKey('books.id', ondelete='CASCADE'))
    book: Mapped['Book'] = relationship()
    comments: Mapped[List['Comment']] = relationship()
