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
from models.category import Category
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from models.engine.config_db import url_object
from models.base_model import BaseModel

class DBStorage():

    __engine = None
    __session = None

    def __init__(self):
        """initialize the storage object"""
        self.__engine = create_engine(url_object)

    def new(self, obj):
        """creates new object"""
        self.__session.add(obj)

    def get(self, class_name, id):
        """get an object from the database by id"""
        return self.__session.get(class_name, id)

    def all(self, class_name=None):
        """get all objects in the database"""
        pass

    def save(self, n=0):
        """save an object to the database"""
        # the function is recursive so that all the updated object can update
        #+ there corresponding updated_at variable
        dirty_objs = list(self.__session.dirty)
        if n < len(dirty_objs):
            dirty_objs[n].save(n+1)
        self.__session.commit()

    def delete(self, obj):
        """remove an object from the database"""
        self.__session.delete(obj)

    def close(self):
        """close the context for a request session"""
        self.__session.remove()

    def reload(self):
        """create the database tables"""
        BaseModel.metadata.create_all(self.__engine)
        # use the session factory to bind all sessions to the same engine
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        # create a thread safe scoped session that can be used on apps
        #+ that will handle concurrent requests
        Session = scoped_session(sess_factory)
        self.__session = Session()
