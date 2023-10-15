#!/usr/bin/python3

import uuid
from datetime import datetime
import models

time = "%Y-%m-%dT%H:%M:%S.%f"


"""Base Model Class Definition"""


class BaseModel:
    """ This is the base class for all objects"""

    def __init__(self, *args, **kwargs):
        """ Initializes instances of the BaseModel class"""

        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                if key != '__class__':
                    setattr(self, key, value)
        else:
            """
            Generate UUID for id then set created_at
            and updated_at to the current date and time
            """
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()
            models.storage.new(self)
            models.storage.save()

    def __str__(self):

        """ Returns the string representation of an instance. """
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):

        """ Sets updated_at to current date and time. """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):

        """returns a dictionary containing all keys/values of the instance"""
        my_dict = self.__dict__.copy()
        my_dict['created_at'] = self.created_at.isoformat()
        my_dict['updated_at'] = self.updated_at.isoformat()
        my_dict['__class__'] = self.__class__.__name__
        return my_dict
