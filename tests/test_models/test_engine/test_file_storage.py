#!/usr/bin/python3
"""
This module contains the various test cases for the base module
"""


import datetime
from models import base_model
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


class FileStorageTest(unittest.TestCase):
    """
    This class contains various test cases to test the BaseModel class
    """

    def setUp(self):
        """
        Make an instance of the base model class to be used for testing
        out the class
        """
        self.bm = BaseModel()
        try:
            os.rename("file.json", "tmp")
        except Exception:
            pass

    def test_mod_doc(self):
        """Test module documentation"""
        self.assertNotEqual(len(base_model.__doc__.split()), 0)

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
        self.assertTrue(BaseModel())

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
        b = BaseModel()
        self.assertTrue(isinstance(b, BaseModel))

    def test_uuid(self):
        """test uid"""
        b1 = BaseModel()
        b2 = BaseModel()
        self.assertTrue(isinstance(b1.id, str))
        self.assertFalse(b1.id == b2.id)

    def test_created_at(self):
        """tests createdat and updated_at"""
        b = BaseModel()
        self.assertIsInstance(b.created_at, datetime.datetime)
        self.assertIsInstance(b.updated_at, datetime.datetime)

    def test_save(self):
        """tests the save function"""
        b = BaseModel()
        init = b.updated_at
        sleep(1)
        b.save()
        self.assertTrue(os.path.isfile("file.json"))
        self.assertNotEqual(init, b.updated_at)
        with self.assertRaises(TypeError):
            b.save(None)

    def test_file_path(self):
        """test wether file path exists"""
        with self.assertRaises(AttributeError):
            FileStorage.__filepath

    def test_file_reload(self):
        """test wether reload works properly"""
        self.assertFalse(FileStorage().reload())

    def test_file_save(self):
        """test wether save works properly"""
        self.assertFalse(FileStorage().save())

    def test_file_new(self):
        """test wehter new works properly"""
        self.assertFalse(FileStorage().new(BaseModel()))

    def test_file_all(self):
        """test wether all works properly"""
        self.assertTrue(FileStorage().all())

    def test_file_path(self):
        """test wether file path exists"""
        with self.assertRaises(AttributeError):
            FileStorage.__objects

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


class TestFileStorage(unittest.TestCase):
    """Class for testing FileStorage Class"""

    def setUp(self):
        """
        Make an instance of the base model class to be used for testing
        out the class
        """
        self.storage = FileStorage()
        try:
            os.rename("file.json", "tmp")
        except Exception:
            pass

    def test_init(self):
        self.assertIsInstance(self.storage, FileStorage)
        self.assertIsInstance(FileStorage._FileStorage__file_path, str)
        self.assertIsInstance(FileStorage._FileStorage__objects, dict)
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_methods(self):
        """tests all methods"""
        # all
        self.assertIsInstance(self.storage.all(), dict)
        with self.assertRaises(TypeError):
            self.storage.all(None)
        b = BaseModel()

        # new
        self.storage.new(b)
        id = "BaseModel." + b.id
        self.assertIn(id, self.storage.all())
        with self.assertRaises(AttributeError):
            self.storage.new(1)
        with self.assertRaises(AttributeError):
            self.storage.new(1)
        with self.assertRaises(TypeError):
            self.storage.new(b, 1)

        # save
        self.storage.save()
        with open("file.json", "r") as file:
            self.assertIn(id, file.readline())
        with self.assertRaises(TypeError):
            self.storage.save(1)

        # reload
        self.storage.reload()
        self.assertIn(id, self.storage.all())
        with self.assertRaises(TypeError):
            self.storage.reload(1)

    def tearDown(self):
        try:
            os.remove("file.json")
        except Exception:
            pass
        try:
            os.rename("tmp", "file.json")
        except Exception:
            pass
