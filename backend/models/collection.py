#!/usr/bin/python3
"""This file defines the Collection class"""
from models.base_model import BaseModel
from sqlalchemy.orm import Mapped, mapped_column


class Collection(BaseModel):
    """Collection class"""
    __tablename__ = 'collections'
    name: Mapped[str] = mapped_column(nullable=False)
