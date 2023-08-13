#!/usr/bin/python3
"""Defines unittests for console.py."""


from console import HBNBCommand
from models.engine.file_storage import FileStorage
from models import storage
import unittest
import datetime
from unittest.mock import patch
import sys
from io import StringIO
import re
import os


class TestConsole(unittest.TestCase):
    """class contains tests cases for the console"""

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

    def test_prompt(self):
        self.assertEqual("(hbnb) ", HBNBCommand.prompt)

    def test_help_quit(self):
        h = "Quit command to exit the program."
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help quit"))
            self.assertEqual(h, output.getvalue().strip())

    def test_help_create(self):
        h = ("""Creates a new instance of BaseModel""")
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help create"))
            self.assertEqual(h, output.getvalue().strip())

    def test_help_EOF(self):
        h = "Exits out of the program console"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help EOF"))
            self.assertEqual(h, output.getvalue().strip())

    def test_help_show(self):
        h = ("""Print string representation of object based on class name
        and ID""")
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help show"))
            self.assertEqual(h, output.getvalue().strip())

    def test_help_destroy(self):
        h = ("Deletes an instance based on the class name and id")
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help destroy"))
            self.assertEqual(h, output.getvalue().strip())

    def test_help_all(self):
        h = ("""Print string representation of all instances based or not on
        the class name""")
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help all"))
            self.assertEqual(h, output.getvalue().strip())

    def test_help_count(self):
        h = ("""Count the number of instances in the storage system""")
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help count"))
            self.assertEqual(h, output.getvalue().strip())

    def test_help_update(self):
        h = ("Updates an instance based on the class name")
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help update"))
            self.assertEqual(h, output.getvalue().strip())

    def test_help(self):
        h = ("Documented commands (type help <topic>):\n"
             "========================================\n"
             "EOF  all  count  create  destroy  help  quit  show  update")
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help"))
            self.assertEqual(h, output.getvalue().strip())

    def test_empty_line(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(""))
            self.assertEqual("", output.getvalue().strip())

    def test_help_quit(self):
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("help quit")
            self.assertTrue(output != "")

    def test_create_missing_class(self):
        correct = "** class name missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create"))
            self.assertEqual(correct, output.getvalue().strip())

    def test_create_invalid_class(self):
        correct = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create MyModel"))
            self.assertEqual(correct, output.getvalue().strip())

    def test_create_invalid_syntax(self):
        correct = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("MyModel.create()"))
            self.assertEqual(correct, output.getvalue().strip())

    def test_create_object(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            self.assertLess(0, len(output.getvalue().strip()))
            testKey = "BaseModel.{}".format(output.getvalue().strip())
            self.assertIn(testKey, storage.all().keys())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create User"))
            self.assertLess(0, len(output.getvalue().strip()))
            testKey = "User.{}".format(output.getvalue().strip())
            self.assertIn(testKey, storage.all().keys())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create State"))
            self.assertLess(0, len(output.getvalue().strip()))
            testKey = "State.{}".format(output.getvalue().strip())
            self.assertIn(testKey, storage.all().keys())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create City"))
            self.assertLess(0, len(output.getvalue().strip()))
            testKey = "City.{}".format(output.getvalue().strip())
            self.assertIn(testKey, storage.all().keys())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            self.assertLess(0, len(output.getvalue().strip()))
            testKey = "Amenity.{}".format(output.getvalue().strip())
            self.assertIn(testKey, storage.all().keys())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            self.assertLess(0, len(output.getvalue().strip()))
            testKey = "Place.{}".format(output.getvalue().strip())
            self.assertIn(testKey, storage.all().keys())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Review"))
            self.assertLess(0, len(output.getvalue().strip()))
            testKey = "Review.{}".format(output.getvalue().strip())
            self.assertIn(testKey, storage.all().keys())

    def test_quit(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertTrue(HBNBCommand().onecmd("quit"))

    def test_EOF(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertTrue(HBNBCommand().onecmd("EOF"))

    def test_show(self):
        id = None
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create BaseModel")
            id = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd(f"show {id}")
            self.assertTrue(output.getvalue().strip() != "")
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd(f"show 1234567")
            self.assertEqual(output.getvalue().strip(),
                             "** class doesn't exist **")
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd(f"show User 1234567")
            self.assertEqual(output.getvalue().strip(),
                             "** no instance found **")
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd(f"show User")
            self.assertEqual(output.getvalue().strip(),
                             "** instance id missing **")

    def test_destroy(self):
        id = None
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create BaseModel")
            id = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd(f"destroy {id}")
            self.assertTrue(output.getvalue().strip() != "")
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd(f"destroy 1234567")
            self.assertEqual(output.getvalue().strip(),
                             "** class doesn't exist **")
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd(f"destroy User 1234567")
            self.assertEqual(output.getvalue().strip(),
                             "** no instance found **")
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd(f"destroy User")
            self.assertEqual(output.getvalue().strip(),
                             "** instance id missing **")

    def test_all(self):
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create BaseModel")
            id = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("all")
            self.assertTrue(output.getvalue().strip() != "")
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("all 1234567")
            self.assertEqual(output.getvalue().strip(),
                             "** class doesn't exist **")

    def test_update(self):
        id = None
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create User")
            id = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd(f'update User {id} email "aibnb@mail.com"')
            self.assertTrue(output.getvalue().strip() == "")
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd(f"update 1234567")
            self.assertEqual(output.getvalue().strip(),
                             "** class doesn't exist **")
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd(f"update User 1234567")
            self.assertEqual(output.getvalue().strip(),
                             "** no instance found **")
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd(f"update User {id}")
            self.assertEqual(output.getvalue().strip(),
                             "** attribute name missing **")
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd(f"update User {id} email")
            self.assertEqual(output.getvalue().strip(),
                             "** value missing **")

    def test_class_all(self):
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("User.all()")
            self.assertTrue(output.getvalue().strip() != "")
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd(f"Hello.all()")
            self.assertEqual(output.getvalue().strip(),
                             "** class doesn't exist **")

    def test_class_show(self):
        id = None
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create User")
            id = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd(f"User.show({id})")
            self.assertTrue(output.getvalue().strip() != "")
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd(f"Hello.show({id})")
            self.assertEqual(output.getvalue().strip(),
                             f"** class doesn't exist **")
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd(f"User.show()")
            self.assertEqual(output.getvalue().strip(),
                             "** no instance found **")

    def test_class_count(self):
        with patch("sys.stdout", new=StringIO()) as output:
            for _ in range(5):
                HBNBCommand().onecmd("create User")
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("User.count()")
            self.assertTrue(int(output.getvalue().strip()) >= 5)
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd(f"Hello.count()")
            self.assertEqual(output.getvalue().strip(),
                             "** class doesn't exist **")

    def test_class_destroy(self):
        id = None
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create User")
            id = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd(f"User.destroy({id})")
            self.assertTrue(output.getvalue().strip() != "")
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd(f"Hello.destroy({id})")
            self.assertEqual(output.getvalue().strip(),
                             f"** class doesn't exist **")
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd(f"User.destroy()")
            self.assertEqual(output.getvalue().strip(),
                             "** no instance found **")

    def test_class_update(self):
        id = None
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create User")
            id = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            q_id = f'"{id}"'
            HBNBCommand().onecmd(
                f'User.update({q_id} "email" "aibnb@mail.com")')
            self.assertEqual(output.getvalue().strip(), '')
        with patch("sys.stdout", new=StringIO()) as output:
            q_id = f'"{id}"'
            HBNBCommand().onecmd(
                f"""User.update({q_id}, {{'first_name': "John", "age": 89}})""")
            self.assertEqual(output.getvalue().strip(), '')
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand()\
                .onecmd(f'U.update({q_id} "email" "aibnb@mail.com")')
            self.assertEqual(output.getvalue().strip(),
                             "** class doesn't exist **")
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand()\
                .onecmd(f'User.update({id} "email" "aibnb@mail.com")')
            self.assertEqual(output.getvalue().strip(),
                             "** no instance found **")
        with patch("sys.stdout", new=StringIO()) as output:
            q_id = f'"{id}"'
            HBNBCommand().onecmd(f'User.update({q_id})')
            self.assertEqual(output.getvalue().strip(),
                             "")
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd(f"update User {id} email")
            self.assertEqual(output.getvalue().strip(),
                             "** value missing **")

    def tearDown(self):
        try:
            os.remove("file.json")
        except Exception:
            pass
        try:
            os.rename("tmp", "file.json")
        except Exception:
            pass
