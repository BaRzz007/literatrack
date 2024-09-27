#!/usr/bin/python3
"""
User statistics module
"""

from models.base_model import BaseModel


class UserStat(BaseModel):
    """
    User statistics class
    """
    user_id = ""
    speed = 0
    reading = 0
    completed = 0
    completion_rate = 0
