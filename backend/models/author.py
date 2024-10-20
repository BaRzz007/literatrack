#!/usr/bin/env python3
"""This file defines the Author class"""
from models.base_model import BaseModel
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column


class Author(BaseModel):
    """Author class"""
    __tablename__ = 'authors'
    firstname: Mapped[str] = mapped_column(String(20), nullable=True)
    lastname: Mapped[str] = mapped_column(String(20), nullable=True)
    fullname: Mapped[str] = mapped_column(String(60))
    nationality: Mapped[str] = mapped_column(String(20), nullable=True)
