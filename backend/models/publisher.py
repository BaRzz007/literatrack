#!/usr/bin/python3
"""This ile defines the Publisher class"""
from models.base_model import BaseModel
from sqlalchemy.orm import Mapped, mapped_column


class Publisher(BaseModel):
    """Publisher class"""
    __tablename__ = 'publishers'
    name: Mapped[str]
    address: Mapped[str]
