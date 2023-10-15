#!/usr/bin/python3
""" BaseModel serves as the blueprint, establishing shared
    attributes and methods for its derived classes. """

import uuid
from datetime import datetime
import models


class BaseModel:
    """base model class"""

    def __init__(self, *args, **kwargs):
        """Generate a fresh instance of the BaseModel class,
        customizing its attributes and behavior by supplying
        both positional arguments and keyword-based parameters
        during instantiation. """

        if kwargs:
            for key, val in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    val = datetime.strptime(val, "%Y-%m-%dT%H:%M:%S.%f")
                if key != '__class__':
                    setattr(self, key, val)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self):
        """ representation string  of base model"""
        return "[{}] ({}) {}".format(
            type(self).__name__, self.id, self.__dict__)

    def save(self):
        """saved class"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """returns a dictt containing all keys and values of object"""
        obj_dictt = dict(self.__dict__)
        obj_dictt['__class__'] = type(self).__name__
        obj_dictt['created_at'] = self.created_at.isoformat()
        obj_dictt['updated_at'] = self.updated_at.isoformat()
        return obj_dictt
