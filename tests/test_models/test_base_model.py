#!/usr/bin/python3
from unittest import TestCase


class TestBaseModel(TestCase):
    def setUp(self) -> None:
        """ """
        from models.base_model import BaseModel
        self.base = BaseModel()
        return super().setUp()
    
    def test_init(self):
        """ """
        from models.base_model import BaseModel
        self.assertTrue(isinstance(self.base, BaseModel))
