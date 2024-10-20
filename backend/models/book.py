#!/usr/bin/env python3
"""Book class file"""
from typing import List
from models.base_model import BaseModel
from sqlalchemy import String, ForeignKey, Table, Column, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
import datetime


book_authors = Table(
        'book_authors',
        BaseModel.metadata,
        Column('author_id', ForeignKey('authors.id', ondelete='CASCADE'), primary_key=True),
        Column('book_id', ForeignKey('books.id', ondelete='CASCADE'), primary_key=True))

book_category = Table(
        'book_category',
        BaseModel.metadata,
        Column('book_id', ForeignKey('books.id', ondelete='CASCADE'), primary_key=True),
        Column('category_id', ForeignKey('category.id', ondelete='CASCADE'), primary_key=True))


class Book(BaseModel):
    """book class"""
    __tablename__ = 'books'
    title: Mapped[str] = mapped_column(String(50))
    publish_date: Mapped[datetime.datetime]
    lang: Mapped[str] = mapped_column(String(5), default='en')
    page_count: Mapped[int]
    isbn_10: Mapped[str] = mapped_column(String(10), nullable=True)
    isbn_13: Mapped[str] = mapped_column(String(13), nullable=True)
    cover_img_url: Mapped[str] = mapped_column(String(1024), nullable=True)
    publisher_id: Mapped[str] = mapped_column(ForeignKey('publishers.id'))
    published_by: Mapped['Publisher'] = relationship()
    authors: Mapped[List['Author']] = relationship(secondary=book_authors, passive_deletes=True)
    categories: Mapped[List['Category']] = relationship(
            secondary=book_category,
            passive_deletes=True,
            back_populates='books')
