#!/usr/bin/python3

from models.base_model import BaseModel
from models.amenity import Amenity
from datetime import datetime
import unittest


class TestAmenity(unittest.TestCase):

    # Create an instance of Amenity
    def test_instance_creation(self):
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)

    # Set the name attribute of an instance of Amenity
    def test_set_name_attribute(self):
        amenity = Amenity()
        amenity.name = "Pool"
        self.assertEqual(amenity.name, "Pool")

    # Call the to_dict method on an instance of Amenity
    def test_to_dict_method(self):
        amenity = Amenity()
        amenity.name = "Gym"
        amenity_dict = amenity.to_dict()
        self.assertIsInstance(amenity_dict, dict)
        self.assertEqual(amenity_dict['name'], "Gym")

    # Create an instance of Amenity with no arguments
    def test_instance_creation_no_arguments(self):
        amenity = Amenity()
        self.assertIsNotNone(amenity.id)
        self.assertIsNotNone(amenity.created_at)
        self.assertIsNotNone(amenity.updated_at)

    # Create an instance of Amenity with a dictionary containing all attributes
    def test_instance_creation_with_dictionary(self):
        amenity_dict = {
            'id': '123',
            'created_at': '2022-01-01T00:00:00.000000',
            'updated_at': '2022-01-01T00:00:00.000000',
            'name': 'Sauna'
        }
        amenity = Amenity(**amenity_dict)
        self.assertEqual(amenity.id, '123')
        self.assertEqual(amenity.created_at,
                         datetime.strptime('2022-01-01T00:00:00.000000',
                                           '%Y-%m-%dT%H:%M:%S.%f'))
        self.assertEqual(amenity.updated_at,
                         datetime.strptime('2022-01-01T00:00:00.000000',
                                           '%Y-%m-%dT%H:%M:%S.%f'))
        self.assertEqual(amenity.name, 'Sauna')
