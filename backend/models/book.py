"""Book class file"""
from models.base_model import BaseModel
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
import datetime


class Book(BaseModel):
    """book class"""
    __tablename__ = 'books'
    title: Mapped[str]
    publish_date: Mapped[datetime.datetime]
    lang: Mapped[str] = mapped_column(default='en')
    page_count: Mapped[int]
    isbn_10: Mapped[str] = mapped_column(String(10))
    isbn_13: Mapped[str] = mapped_column(String(13))
    cover_img_url: Mapped[str]

