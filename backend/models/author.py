#!/usr/bin/env python3
"""This file defines the Author class"""
from models.base_model import BaseModel
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column


class Author(BaseModel):
    """Author class"""
    __tablename__ = 'authors'
    firstname: Mapped[str] = mapped_column(String(20))
    lastname: Mapped[str] = mapped_column(String(20))
    fullname: Mapped[str] = mapped_column(String(60),
            default=lambda self: f'{self.firstname} {self.lastname}')
    nationality: Mapped[str] = mapped_column(String(20))
