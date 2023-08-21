#!/usr/bin/python3
""" """
from models.base_model import BaseModel
from datetime import timedelta


class Report(BaseModel):
    """
    Report class
    """
    user_id = ""
    month = ""
    year = ""
    # duration in days
    __duration = timedelta(days=0)
    num_books_started = 0
    num_books_completed = 0
    completion_rate = 0

    @property
    def duration(self):
        """
        returns the duration timedelta
        """
        return self.__duration

    @duration.setter
    def duration(self, days):
        """
        Sets duration in days
        """
        self.__duration = timedelta(days=days)
