#!/usr/bin/python3
"""
Contains the TestStateDocs classes
"""

from datetime import datetime
import inspect
from models import state
from models.base_model import BaseModel
import unittest
State = state.State


class TestState(unittest.TestCase):

    # Create an instance of State
    def test_instance_of_BaseModel(self):
        state = State()
        self.assertIsInstance(state, BaseModel)

    # Set the name attribute of an instance of State
    def test_set_name_attribute(self):
        state = State()
        state.name = "California"
        self.assertEqual(state.name, "California")

    # Call the to_dict method on an instance of State
    def test_to_dict_method(self):
        state = State()
        state.name = "California"
        state_dict = state.to_dict()
        self.assertEqual(state_dict['name'], "California")
        self.assertEqual(state_dict['__class__'], "State")

    # Create an instance of State with no arguments
    def test_no_arguments(self):
        state = State()
        self.assertIsNotNone(state.id)
        self.assertIsNotNone(state.created_at)
        self.assertIsNotNone(state.updated_at)

    # Create an instance of State with a created_at or updated_at
    def test_invalid_datetime_format(self):
        with self.assertRaises(ValueError):
            state = State(created_at="2022-01-01")
