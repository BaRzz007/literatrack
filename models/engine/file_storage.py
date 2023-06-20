#!/usr/bin/python3
""" """
import json
from models.base_model import BaseModel
from models.user import User
from models.author import Author
from models.book import Book, BookAuthor
from models.review import Review
from models.comment import Comment


classes = {"BaseModel": BaseModel,
           "User": User,
           "Book": Book,
           "Author": Author,
           "BookAuthor": BookAuthor,
           "Review": Review,
           "Comment": Comment}


class FileStorage:
    """ """
    __objects = {}
    __file = "file.json"

    def new(self, obj):
        """Add new object to storage dictionary"""
        if obj is not None:
            self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def all(self, cls=None):
        """Returns a dictionary of all objects stored in storage instance"""
        if cls is not None:
            return {key: obj for key, obj in self.__objects.items()
                    if obj.__class__ == cls}
        return self.__objects

    def get(self, cls, id):
        """Returns an object instance or None if it doesn't exist"""
        return self.all().get(f"{cls.__name__}.{id}")

    def save(self):
        """Save objects to file"""
        dict_objs = {key: obj.to_dict() for key, obj in self.__objects.items()}
        try:
            with open(self.__file, "w") as file:
                json.dump(dict_objs, file)
        except Exception as e:
            print(f"Cannot save to {self.__file}, {e}")

    def delete(self, obj=None):
        """Remove an object from storage"""
        if obj is not None:
            key = f"{obj.to_dict['__class__']}.{obj.id}"
        if key in self.all().keys():
            del self.__objects[key]

    def reload(self):
        """Deserialize obj from json"""
        try:
            with open(self.__file, "r") as file:
                temp = json.load(file)
        except Exception as e:
            return
        self.__objects = {key: classes[val["__class__"]](**val)
                          for key, val in temp.items()}
