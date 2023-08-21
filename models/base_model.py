#!/usr/bin/python3
"""base_model module"""
import uuid
from datetime import datetime
from datetime import timedelta

timefmt = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    """base_model class"""

    def __init__(self, *args, **kwargs):
        """Innitialization of model instance"""
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
            if kwargs.get("created_at", None) and type(self.created_at) is str:
                self.created_at = datetime.strptime(kwargs["created_at"], timefmt)
            else:
                self.created_at = datetime.utcnow()

            if kwargs.get("updated_at", None) and type(self.updated_at) is str:
                self.updated_at = datetime.strptime(kwargs["updated_at"], timefmt)
            else:
                self.updated_at = datetime.utcnow()

            if kwargs.get("duration", None):
                self.duration = kwargs["duration"]

            if kwargs.get("id", None) is None:
                self.id = str(uuid.uuid4())
        else:
            time = datetime.utcnow()
            self.id = str(uuid.uuid4())
            self.created_at = time
            self.updated_at = time

    def __str__(self):
        """String representaton of instance"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
    
    def save(self):
        """ """
        from models import storage
        self.updated_at = datetime.utcnow()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """ """
        temp_dict = self.__dict__.copy()
        if "created_at" in temp_dict.keys():
            temp_dict["created_at"] = temp_dict["created_at"].strftime(timefmt)
        if "updated_at" in temp_dict.keys():
            temp_dict["updated_at"] = temp_dict["updated_at"].strftime(timefmt)
        if f"_{self.__class__.__name__}__duration" in temp_dict.keys():
            temp_dict["duration"] = self.duration.days
        del temp_dict[f"_{self.__class__.__name__}__duration"]
        temp_dict["__class__"] = self.__class__.__name__
        if "_sa_instance_state" in temp_dict:
            del temp_dict["_sa_instance_state"]
        return temp_dict

    def delete(self):
        """ """
        from models import storage
        storage.delete(self)
        storage.save()
