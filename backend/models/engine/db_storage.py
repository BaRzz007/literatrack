"""Database storage class"""
from sqlalchemy import create_engine
from config_db import url_object

class DBStorage():

    def __init__():
        """initialize the storage object"""
        __engine = create_engine(url_object)


    def new():
        """creates new object"""
        pass

    def get(id):
        """get an object from the database by id"""
        pass

    def all(class_name=""):
        """get all objects in the database"""
        pass

    def save():
        """save an object to the database"""
        pass

    def delete(id):
        """remove an object from the database"""
        pass

    def create_tables():
        """create the database tables"""
        pass
