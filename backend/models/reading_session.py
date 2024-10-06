#!/usr/bin/python3
"""this file defines the ReadingSession class"""
from models.base_model import BaseModel
from sqlalchemy.orm import Mapped, mapped_column
import datetime


class ReadingSession(BaseModel):
    """readingsession class"""
    __tablename__ = 'reading_sessions'
    start_date: Mapped[datetime.datetime]
    end_date: Mapped[datetime.datetime]
    status: Mapped[str]
    current_page: Mapped[int]
    privacy: Mapped[str]
