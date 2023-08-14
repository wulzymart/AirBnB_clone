#!/usr/bin/python3
"""
This module contains the various test cases for the base module
"""


import datetime
from models import review
from models.review import Review
import os
from time import sleep
import unittest


class ReviewTest(unittest.TestCase):
    """
    This class contains various test cases to test the Review class
    """

    def setUp(self):
        """
        Make an instance of the base model class to be used for testing
        out the class
        """
        self.bm = Review()
        try:
            os.rename("file.json", "tmp")
        except Exception:
            pass

    def test_mod_doc(self):
        """Test module documentation"""
        self.assertNotEqual(len(review.__doc__.split()), 0)

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
        self.assertTrue(Review())

    def test_base_init_r2(self):
        """Test case"""
        dic = self.bm.to_dict()
        b = Review(**dic)
        self.assertTrue(b != self.bm)

    def test_base_init_r3(self):
        """Test case"""
        b = Review(5)
        self.assertTrue(Review(5))

    def test_instance(self):
        """Test if it produces an instance"""
        b = Review()
        self.assertTrue(isinstance(b, Review))

    def test_uuid(self):
        """test uid"""
        b1 = Review()
        b2 = Review()
        self.assertTrue(isinstance(b1.id, str))
        self.assertFalse(b1.id == b2.id)

    def test_created_at(self):
        """tests createdat and updated_at"""
        b = Review()
        self.assertIsInstance(b.created_at, datetime.datetime)
        self.assertIsInstance(b.updated_at, datetime.datetime)

    def test_save(self):
        """tests the save function"""
        b = Review()
        init = b.updated_at
        sleep(1)
        b.save()
        self.assertTrue(os.path.isfile("file.json"))
        self.assertNotEqual(init, b.updated_at)
        with self.assertRaises(TypeError):
            b.save(None)

    def test_review_attr(self):
        """test the reviews attributes"""
        obj = Review()
        self.assertEqual(obj.place_id, "")
        self.assertEqual(obj.user_id, "")
        self.assertEqual(obj.text, "")

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
