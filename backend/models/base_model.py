#!/usr/bin/env python3
"""base_model module"""
import uuid
from datetime import datetime, timedelta
from sqlalchemy import DateTime, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


timefmt = "%Y-%m-%dT%H:%M:%S.%f"

class BaseModel(DeclarativeBase):
    """base_model class"""
    id: Mapped[str] = mapped_column(
            String(36),
            primary_key=True,
            nullable=False)

    created_at: Mapped[datetime] = mapped_column(
            DateTime,
            nullable=False)

    updated_at: Mapped[datetime] = mapped_column(
            DateTime,
            nullable=False)

    def __init__(self, *args, **kwargs):
        """Innitialization of model instance"""
        if kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)
        time = datetime.now()
        self.id = str(uuid.uuid4())
        self.created_at = time
        self.updated_at = time
        super().__init__()
        from models import storage
        storage.new(self)
        storage.save()

    def __str__(self):
        """String representaton of instance"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.to_dict()}"
    
    def save(self, n=0):
        """save object to the database"""
        from models import storage
        self.updated_at = datetime.now()
        # storage.new(self)
        storage.save(n)

    def to_dict(self):
        """serializes an object to dictionary"""
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
