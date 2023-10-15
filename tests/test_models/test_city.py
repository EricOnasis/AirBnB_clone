#!/usr/bin/python3

from models.base_model import BaseModel
from models.city import City
import unittest


class TestCity(unittest.TestCase):

    # create a City instance with state_id and name
    def setUp(self):
        self.city = City(state_id="state123", name="Nairobi City")

    # check that the City instance has state_id and name attributes
    def test_check_city_instance_attribute_values(self):
        city = City(state_id="123", name="New York")
        self.assertEqual(city.state_id, "123")
        self.assertEqual(city.name, "New York")

    # create a City instance with empty state_id and name
    def test_create_city_instance_with_empty_attributes(self):
        city = City(state_id="", name="")
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")

    # create a City instance with non-string state_id and name
    def test_create_city_instance_with_non_string_attributes(self):
        city = City(state_id=123, name=456)
        self.assertEqual(city.state_id, 123)
        self.assertEqual(city.name, 456)
