#!/usr/bin/env python3
"""This file defines the Note class"""
from models.base_model import BaseModel
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
import datetime


class Note(BaseModel):
    """Note class"""
    __tablename__ = 'notes'
    page_number: Mapped[int]
    note: Mapped[str] = mapped_column(String(1000))
    privacy: Mapped[str] = mapped_column(String(10), default='public')
    book_id: Mapped[str] = mapped_column(ForeignKey('books.id', ondelete='CASCADE'))
    book: Mapped['Book'] = relationship()
    user_id: Mapped[str] = mapped_column(ForeignKey('users.id', ondelete='CASCADE'))
    user: Mapped['User'] = relationship()
