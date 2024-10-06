#!/usr/bin/python3
"""This file defines the Note class"""
from models.base_model import BaseModel
from sqlalchemy.orm import Mapped, mapped_column
import datetime


class Note(BaseModel):
    """Note class"""
    __tablename__ = 'notes'
    page_number: Mapped[int] = mapped_column(nullable=False)
    note: Mapped[str]
    date: Mapped[datetime.datetime]
    privacy: Mapped[str] = mapped_column(default='public')
