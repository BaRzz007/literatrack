#!/usr/bin/env python3
"""This file defines the Collection class"""
from typing import List
from models.base_model import BaseModel
from sqlalchemy import String, ForeignKey, Table, Column
from sqlalchemy.orm import Mapped, mapped_column, relationship


book_collection = Table(
        'book_collection',
        BaseModel.metadata,
        Column('book_id', ForeignKey('books.id', ondelete='CASCADE'), primary_key=True),
        Column('collection_id', ForeignKey('collections.id', ondelete='CASCADE'), primary_key=True))


class Collection(BaseModel):
    """Collection class"""
    __tablename__ = 'collections'
    name: Mapped[str] = mapped_column(String(20))
    user_id: Mapped[str] = mapped_column(ForeignKey('users.id', ondelete='CASCADE'))
    user: Mapped['User'] = relationship(back_populates='collections')
    books: Mapped[List['Book']] = relationship(secondary=book_collection, passive_deletes=True)
