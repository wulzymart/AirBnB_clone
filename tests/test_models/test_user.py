#!/usr/bin/python3
"""
This module contains the various test cases for the base module
"""


import datetime
from models import user
from models.user import User
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
        self.u = User()
        try:
            os.rename("file.json", "tmp")
        except Exception:
            pass

    def test_mod_doc(self):
        """Test module documentation"""
        self.assertNotEqual(len(user.__doc__.split()), 0)

    def test_doc(self):
        """Test class doc"""
        self.assertNotEqual(len(self.u.__doc__.split()), 0)

    def test_save(self):
        """Test class doc"""
        self.assertNotEqual(len(self.u.save.__doc__.split()), 0)

    def test_to_dict(self):
        """Test class doc"""
        test_dict = self.u.to_dict()
        self.assertNotEqual(len(self.u.to_dict.__doc__.split()), 0)
        self.assertIsInstance(test_dict, dict)
        self.assertIn("__class__", test_dict)
        self.assertIsInstance(test_dict["created_at"], str)
        self.assertIsInstance(test_dict["updated_at"], str)

    def test_str(self):
        """Test class doc"""
        self.assertNotEqual(len(str(self.u)), 0)
        self.assertRegex(str(self.u), r"^\[[a-z-A-Z]+\] \(.+\) {.+}$")

    def test_user_init_r1(self):
        """Test case"""
        self.assertTrue(User())

    def test_user_init_r2(self):
        """Test case"""
        dic = self.u.to_dict()
        b = User(**dic)
        self.assertTrue(b != self.u)

    def test_user_init_r3(self):
        """Test case"""
        b = User(5)
        self.assertTrue(User(5))

    def test_created_at(self):
        """tests createdat and updated_at"""
        b = User()
        self.assertIsInstance(b.created_at, datetime.datetime)
        self.assertIsInstance(b.updated_at, datetime.datetime)

    def test_save(self):
        """tests the save function"""
        b = User()
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
