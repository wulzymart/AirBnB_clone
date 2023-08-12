#!/usr/bin/python3
"""
This module contains the various test cases for the base module
"""


import datetime
from models import base_model
from models import storage
from models import amenity
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


class AmenityTest(unittest.TestCase):
    """
    This class contains various test cases to test the BaseModel class
    """

    def setUp(self):
        """
        Make an instance of the base model class to be used for testing
        out the class
        """
        self.am = Amenity()
        try:
            os.rename("file.json", "tmp")
        except Exception:
            pass

    def test_mod_doc(self):
        """Test module documentation"""
        self.assertNotEqual(len(amenity.__doc__.split()), 0)

    def test_base_doc(self):
        """Test class doc"""
        self.assertNotEqual(len(self.am.__doc__.split()), 0)

    def test_base_save(self):
        """Test class doc"""
        self.assertNotEqual(len(self.am.save.__doc__.split()), 0)

    def test_base_to_dict(self):
        """Test class doc"""
        test_dict = self.am.to_dict()
        self.assertNotEqual(len(self.am.to_dict.__doc__.split()), 0)
        self.assertIsInstance(test_dict, dict)
        self.assertIn("__class__", test_dict)
        self.assertIsInstance(test_dict["created_at"], str)
        self.assertIsInstance(test_dict["updated_at"], str)

    def test_base_str(self):
        """Test class doc"""
        self.assertNotEqual(len(str(self.am)), 0)
        self.assertRegex(str(self.am), r"^\[[a-z-A-Z]+\] \(.+\) {.+}$")

    def test_base_init_r1(self):
        """Test case"""
        self.assertTrue(Amenity())

    def test_base_init_r2(self):
        """Test case"""
        dic = self.am.to_dict()
        b = Amenity(**dic)
        self.assertTrue(b != self.am)

    def test_base_init_r3(self):
        """Test case"""
        b = Amenity(5)
        self.assertTrue(Amenity(5))

    def test_instance(self):
        """Test if it produces an instance"""
        b = Amenity()
        self.assertTrue(isinstance(b, Amenity))

    def test_uuid(self):
        """test uid"""
        b1 = Amenity()
        b2 = Amenity()
        self.assertTrue(isinstance(b1.id, str))
        self.assertFalse(b1.id == b2.id)

    def test_created_at(self):
        """tests createdat and updated_at"""
        b = Amenity()
        self.assertIsInstance(b.created_at, datetime.datetime)
        self.assertIsInstance(b.updated_at, datetime.datetime)

    def test_save(self):
        """tests the save function"""
        b = Amenity()
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
