#!/usr/bin/env python3
"""This file defines the Note class"""
from models.base_model import BaseModel
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
import datetime


class Note(BaseModel):
    """Note class"""
    __tablename__ = 'notes'
    page_number: Mapped[int] = mapped_column(nullable=False)
    note: Mapped[str] = mapped_column(String(1000))
    date: Mapped[datetime.datetime]
    privacy: Mapped[str] = mapped_column(String(10), default='public')
