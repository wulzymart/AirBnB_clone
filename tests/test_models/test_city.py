#!/usr/bin/python3
"""
This module contains the various test cases for the base module
"""


import datetime
from models import base_model
from models import city
from models import storage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models.engine.file_storage import FileStorage
import os
from time import sleep
import unittest


class BaseModelTest(unittest.TestCase):
    """
    This class contains various test cases to test the BaseModel class
    """

    def setUp(self):
        """
        Make an instance of the base model class to be used for testing
        out the class
        """
        self.bm = City()
        try:
            os.rename("file.json", "tmp")
        except Exception:
            pass

    def test_mod_doc(self):
        """Test module documentation"""
        self.assertNotEqual(len(city.__doc__.split()), 0)

    def test_base_doc(self):
        """Test class doc"""
        self.assertNotEqual(len(self.bm.__doc__.split()), 0)

    def test_base_save(self):
        """Test class doc"""
        self.assertNotEqual(len(self.bm.save.__doc__.split()), 0)

    def test_base_to_dict(self):
        """Test class doc"""
        test_dict = self.bm.to_dict()
        self.assertNotEqual(len(self.bm.to_dict.__doc__.split()), 0)
        self.assertIsInstance(test_dict, dict)
        self.assertIn("__class__", test_dict)
        self.assertIsInstance(test_dict["created_at"], str)
        self.assertIsInstance(test_dict["updated_at"], str)

    def test_base_str(self):
        """Test class doc"""
        self.assertNotEqual(len(str(self.bm)), 0)
        self.assertRegex(str(self.bm), r"^\[[a-z-A-Z]+\] \(.+\) {.+}$")

    def test_base_init_r1(self):
        """Test case"""
        self.assertTrue(City())

    def test_base_init_r2(self):
        """Test case"""
        dic = self.bm.to_dict()
        b = BaseModel(**dic)
        self.assertTrue(b != self.bm)

    def test_base_init_r3(self):
        """Test case"""
        b = BaseModel(5)
        self.assertTrue(BaseModel(5))

    def test_instance(self):
        """Test if it produces an instance"""
        b = City()
        self.assertTrue(isinstance(b, BaseModel))

    def test_uuid(self):
        """test uid"""
        b1 = City()
        b2 = City()
        self.assertTrue(isinstance(b1.id, str))
        self.assertFalse(b1.id == b2.id)

    def test_created_at(self):
        """tests createdat and updated_at"""
        b = City()
        self.assertIsInstance(b.created_at, datetime.datetime)
        self.assertIsInstance(b.updated_at, datetime.datetime)

    def test_save(self):
        """tests the save function"""
        b = City()
        init = b.updated_at
        sleep(1)
        b.save()
        self.assertTrue(os.path.isfile("file.json"))
        self.assertNotEqual(init, b.updated_at)
        with self.assertRaises(TypeError):
            b.save(None)

    def tearDown(self):
        """Unset variables"""
        try:
            os.remove("file.json")
        except Exception:
            pass
        try:
            os.rename("tmp", "file.json")
        except Exception:
            pass
