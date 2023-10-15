#!/usr/bin/env python3
"""
TestFileStorage class
"""

import unittest
import os
import json
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):

    def setUp(self):
        """
        Create a FileStorage instance and a BaseModel instance for testing
        """
        self.storage = FileStorage()
        self.model = BaseModel()
        self.storage.new(self.model)

    def tearDown(self):
        """
        Clean up: Remove the JSON file after each test
        """
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_new_method(self):
        """
        Test if the new method adds the instance to the internal dictionary
        """
        key = "{}.{}".format(self.model.__class__.__name__, self.model.id)
        self.assertIn(key, self.storage.all())

    def test_save_method(self):
        """
        Test if the save method serializes instances to the JSON file
        """
        key = "{}.{}".format(self.model.__class__.__name__, self.model.id)
        self.storage.save()
        with open("file.json", "r") as f:
            data = json.load(f)
            self.assertIn(key, data)

    def test_reload_method(self):
        """
        Test if the reload method correctly deserializes
        instances from the JSON file
        """
        self.storage.save()
        self.storage.reload()
        key = "{}.{}".format(self.model.__class__.__name__, self.model.id)
        self.assertIn(key, self.storage.all())

    def test_all_method(self):
        """
        Test if the all method returns a dictionary of class instances
        """
        model1 = BaseModel()
        model2 = BaseModel()
        self.storage.new(model1)
        self.storage.new(model2)
        all_instances = self.storage.all()
        self.assertIn(model1, all_instances.values())
        self.assertIn(model2, all_instances.values())

    def test_to_dict_method(self):
        """
        Test if the to_dict method returns a dict representation
        """
        expected_dict = {
            'id': self.model.id,
            'created_at': self.model.created_at.isoformat(),
            'updated_at': self.model.updated_at.isoformat(),
            '__class__': self.model.__class__.__name__
        }
        self.assertEqual(self.model.to_dict(), expected_dict)


if __name__ == '__main__':
    unittest.main()
