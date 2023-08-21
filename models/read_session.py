#!/usr/bin/python3
""" """
from models.base_model import BaseModel
from datetime import timedelta


class ReadSession(BaseModel):
    """ """
    user_id = ""
    book_id = ""
    __duration = timedelta(days=0)

    @property
    def duration(self):
        """
        returns the duration timedelta
        """
        return self.__duration

    @duration.setter
    def duration(self, days):
        """
        Sets duratiion in days
        """
        self.__duration = timedelta(days=days)
