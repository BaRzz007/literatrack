#!/usr/bin/env python3
"""This ile defines the Category class"""
from typing import List
from models.base_model import BaseModel
from models.book import book_category
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship


class Category(BaseModel):
    """Category class"""
    __tablename__ = 'category'
    name: Mapped[str] = mapped_column(String(50))
    books: Mapped[List['Book']] = relationship(
            secondary=book_category,
            passive_deletes=True,
            back_populates='categories')
