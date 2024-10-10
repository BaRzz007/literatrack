#!/usr/bin/env python3
"""this file defines the ReadingSession class"""
from models.base_model import BaseModel
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
import datetime


class ReadingSession(BaseModel):
    """readingsession class"""
    __tablename__ = 'reading_sessions'
    start_date: Mapped[datetime.datetime]
    end_date: Mapped[datetime.datetime]
    status: Mapped[str] = mapped_column(String(10))
    current_page: Mapped[int]
    privacy: Mapped[str] = mapped_column(String(10), default='public')
