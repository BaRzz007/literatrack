#!/usr/bin/python3
"""notification module"""
from models.base_model import BaseModel


class Notification(BaseModel):
    """Notification class"""
    event = ""
    event_detail = ""
    user_id = ""
    