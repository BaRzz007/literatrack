#!/usr/bin/env python3
"""This ile defines the Publisher class"""
from models.base_model import BaseModel
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column


class Publisher(BaseModel):
    """Publisher class"""
    __tablename__ = 'publishers'
    name: Mapped[str] = mapped_column(String(50))
    address: Mapped[str] = mapped_column(String(100))
