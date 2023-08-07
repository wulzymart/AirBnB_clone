#!/usr/bin/python3
"""
This module contains a class called BaseModel that defines all attrs
and methods for other classes
"""
import datetime
import uuid


class BaseModel():
    """
    This class contains all the functionalities that will be shared
    among all child classes that inherits from it

    args
    Return
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a new base model object
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()
        self.__create(**kwargs)

    def __create(self, **kwargs):
        """
        Create a new BaseModel object from a json representation
        """
        if kwargs:
            for k, v in kwargs.items():
                if k == "__class__":
                    continue
                if k in ["created_at", "updated_at"]:
                    format = "%Y-%m-%dT%H:%M:%S.%f"
                    v = datetime.datetime.strptime(v, format)
                setattr(self, k, v)

    def __str__(self):
        """
        Print a human readable representation of the string object
        """
        return "[{}] ({}) {}".format(type(self).__name__, self.id,
                                     self.__dict__)
    def save(self):
        """
        updates the public instance attribute updated_at with the
        current datetime
        """
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of __dict__
        of the instance
        """
        dic = self.__dict__
        dic["__class__"] = type(self)
        dic["created_at"] = self.created_at.isoformat()
        dic["updated_at"] = self.updated_at.isoformat()
        return dic

