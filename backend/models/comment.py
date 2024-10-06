#!/usr/bin/python3
"""This file defines the Comment class"""
from models.base_model import BaseModel
from sqlalchemy.orm import Mapped, mapped_column
import datetime


class Comment(BaseModel):
    """Comment class"""
    __tablename__ = 'comments'
    comment: Mapped[str]
    date: Mapped[datetime.datetime]
