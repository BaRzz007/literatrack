#!/usr/bin/python3
"""This file defines the Author class"""
from models.base_model import BaseModel
from sqlalchemy.orm import Mapped, mapped_column


class Author(BaseModel):
    """Author class"""
    __tablename__ = 'authors'
    firstname: Mapped[str]
    lastname: Mapped[str]
    fullname: Mapped[str] = mapped_column(
            default=lambda self: f'{self.firstname} {self.lastname}')
    nationality: Mapped[str]
