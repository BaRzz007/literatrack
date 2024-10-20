#!/usr/bin/env python3
"""This file defines the Comment class"""
from models.base_model import BaseModel
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
import datetime


class Comment(BaseModel):
    """Comment class"""
    __tablename__ = 'comments'
    comment: Mapped[str] = mapped_column(String(1000))
    user_id: Mapped[str] = mapped_column(ForeignKey('users.id', ondelete='CASCADE'))
    user: Mapped['User'] = relationship()
    post_id: Mapped[str] = mapped_column(ForeignKey('posts.id', ondelete='CASCADE'))
    post: Mapped['Post'] = relationship(back_populates='comments')
