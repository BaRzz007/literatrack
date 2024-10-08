"""Database storage class"""
from sqlalchemy import create_engine
from models.engine.config_db import url_object
from models.base_model import BaseModel

class DBStorage():

    def __init__(self):
        """initialize the storage object"""
        self.engine = create_engine(url_object)



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
        pass

    def delete(self, id):
        """remove an object from the database"""
        pass

    def reload(self):
        """create the database tables"""
        BaseModel.metadata.create_all(self.engine)
