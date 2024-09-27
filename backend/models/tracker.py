#!/usr/bin/python3
""" """
from models.base_model import BaseModel
from datetime import timedelta


class Tracker(BaseModel):
    """ """
    __duration = timedelta(days=0)
    report_id = ""

    @property
    def duration(self):
        """
        Returns the duration timedelta
        """
        return self.__duration

    @duration.setter
    def duration(self, days):
        """
        Sets duration in days
        """
        self.__duration = timedelta(days=days)
