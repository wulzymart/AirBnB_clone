#!/usr/bin/python3
"""
This module contains the various test cases for the file storage module
"""


import datetime
from models import base_model
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import os
from time import sleep
import unittest


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
