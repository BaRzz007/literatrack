#!/usr/bin/python3
"""user module"""
from models.base_model import BaseModel
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column


class User(BaseModel):
    """User class"""

    __tablename__ = "users"
    email: Mapped[str] = mapped_column(nullable=False)
    username: Mapped[str] = mapped_column(nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    firstname: Mapped[str] = mapped_column(String(20))
    lastname: Mapped[str] = mapped_column(String(20))
