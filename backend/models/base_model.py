#!/usr/bin/python3
"""base_model module"""
import uuid
from datetime import datetime, timedelta
from sqlalchemy import DateTime
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


timefmt = "%Y-%m-%dT%H:%M:%S.%f"

class BaseModel(DeclarativeBase):
    """base_model class"""

    __abstract__ = True

    id: Mapped[str] = mapped_column(
            primary_key=True,
            nullable=False,
            default=lambda: str(uuid.uuid4()))

    created_at: Mapped[datetime] = mapped_column(
            DateTime,
            default=lambda: datetime.now(), nullable=False)

    updated_at: Mapped[datetime] = mapped_column(
            DateTime,
            default=lambda: datetime.now(),
            onupdate=lambda: datetime.now(), nullable=False)

    def __init__(self, *args, **kwargs):
        """Innitialization of model instance"""
        if kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)
        super().__init__()
        time = datetime.now()
        self.id = str(uuid.uuid4())
        self.created_at = time
        self.updated_at = time

    def __str__(self):
        """String representaton of instance"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.to_dict()}"
    
    def save(self):
        """ """
        from models import storage
        self.updated_at = datetime.now()
        # storage.new(self)
        storage.save()

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
