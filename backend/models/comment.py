#!/usr/bin/env python3
"""This file defines the Comment class"""
from models.base_model import BaseModel
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
import datetime


class Comment(BaseModel):
    """Comment class"""
    __tablename__ = 'comments'
    comment: Mapped[str] = mapped_column(String(1000))
    date: Mapped[datetime.datetime]
