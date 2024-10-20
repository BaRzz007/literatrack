#!/usr/bin/env python3
"""user module"""
from typing import List
from models.base_model import BaseModel
from sqlalchemy import String, Table, Column, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship


friendship = Table(
        'friends',
        BaseModel.metadata,
        Column('user_id', ForeignKey('users.id', ondelete='CASCADE'), primary_key=True),
        Column('friend_id', ForeignKey('users.id', ondelete='CASCADE'), primary_key=True))


class User(BaseModel):
    """User class"""

    __tablename__ = "users"
    email: Mapped[str] = mapped_column(String(225))
    username: Mapped[str] = mapped_column(String(20), unique=True)
    password: Mapped[str] = mapped_column(String(1000))
    firstname: Mapped[str] = mapped_column(String(20), nullable=True)
    lastname: Mapped[str] = mapped_column(String(20), nullable=True)
    collections: Mapped[List['Collection']] = relationship(
            back_populates='user',
            cascade='all, delete')
    friends: Mapped[List['User']] = relationship(
            secondary=friendship,
            primaryjoin='User.id==friends.c.user_id',
            secondaryjoin='User.id==friends.c.friend_id',
            backref='friends_of',
            passive_deletes=True)
