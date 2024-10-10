#!/usr/bin/env python3
"""Database storage class"""
import models
from models.user import User
from models.author import Author
from models.book import Book
from models.comment import Comment
from models.post import Post
from models.collection import Collection
from models.note import Note
from models.publisher import Publisher
from models.reading_session import ReadingSession
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from models.engine.config_db import url_object
from models.base_model import BaseModel

class DBStorage():

    __engine = None

    def __init__(self):
        """initialize the storage object"""
        self.__engine = create_engine(url_object)



    def new(self, obj):
        """creates new object"""
        pass

    def get(self, id):
        """get an object from the database by id"""
        pass

    def all(self, class_name=""):
        """get all objects in the database"""
        pass

    def save(self):
        """save an object to the database"""
        # self.__session.commit()

    def delete(self, id):
        """remove an object from the database"""
        pass

    def reload(self):
        """create the database tables"""
        BaseModel.metadata.create_all(self.__engine)
        # sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        # Session = scoped_session(sess_factory)
        # self.__session = Session
