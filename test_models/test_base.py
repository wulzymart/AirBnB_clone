#!/usr/bin/python3
"""
This module contains the various test cases for the base module
"""
import unittest
from models import base_model
from models.base_model import BaseModel


class BaseModelTest(unittest.TestCase):
    """
    This class contains various test cases to test the BaseModel class
    """

    def setUp(self):
        """
        Make an instance of the base model class to be used for testing
        out the class
        """
        self.bm = BaseModel()

    def test_mod_doc(self):
        self.assertNotEqual(len(base_model.__doc__.split()), 0)

    def test_base_doc(self):
        self.assertNotEqual(len(self.bm.__doc__.split()), 0)

    def test_base_save(self):
        self.assertNotEqual(len(self.bm.save.__doc__.split()), 0)

    def test_base_to_dict(self):
        self.assertNotEqual(len(self.bm.to_dict.__doc__.split()), 0)

    def test_base_str(self):
        self.assertNotEqual(len(str(self.bm)), 0)

    def test_base_init_r1(self):
        self.assertTrue(BaseModel())

    def test_base_init_r2(self):
        dic = self.bm.to_dict()
        self.assertTrue(BaseModel(**dic))

    def test_base_init_r3(self):
        self.assertTrue(BaseModel(5))

    def test_base_init_w1(self):
        self.assertTrue(bm.
