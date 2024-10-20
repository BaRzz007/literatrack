#!/usr/bin/env python3
"""this file defines the ReadingSession class"""
from models.base_model import BaseModel
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
import datetime


class ReadingSession(BaseModel):
    """readingsession class"""
    __tablename__ = 'reading_sessions'
    start_date: Mapped[datetime.datetime]
    end_date: Mapped[datetime.datetime]
    status: Mapped[str] = mapped_column(String(10))
    current_page: Mapped[int] = mapped_column(default=1)
    privacy: Mapped[str] = mapped_column(String(10), default='public')
    book_id: Mapped[str] = mapped_column(ForeignKey('books.id', ondelete='CASCADE'))
    book: Mapped['Book'] = relationship()
    user_id: Mapped[str] = mapped_column(ForeignKey('users.id', ondelete='CASCADE'))
    user: Mapped['User'] = relationship()
