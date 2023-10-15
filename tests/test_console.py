#!/usr/bin/env python3
"""TestHBNBCommand class"""

import unittest
import sys
from unittest import TestCase
from models.base_model import BaseModel
from models import storage
from console import HBNBCommand
from console import HBNBCommand
from unittest.mock import patch
from io import StringIO


import unittest


class TestHBNBCommand(unittest.TestCase):

    # create instance of a class and save it
    def test_create_instance_and_save(self):
        command = HBNBCommand()
        command.do_create("BaseModel")
        instance_id = list(storage.all().keys())[0]
        self.assertIsNotNone(storage.all()[instance_id])

    # class name missing
    def test_class_name_missing(self):
        command = HBNBCommand()
        with patch('sys.stdout', new=StringIO()) as fake_out:
            command.do_create("")
            self.assertEqual(fake_out.getvalue(),
                             "** class name missing **\n")

    # class doesn't exist
    def test_class_doesnt_exist(self):
        command = HBNBCommand()
        with patch('sys.stdout', new=StringIO()) as fake_out:
            command.do_create("InvalidClass")
            self.assertEqual(fake_out.getvalue(),
                             "** class doesn't exist **\n")

    # instance id missing
    def test_instance_id_missing(self):
        command = HBNBCommand()
        with patch('sys.stdout', new=StringIO()) as fake_out:
            command.do_show("BaseModel")
            self.assertEqual(fake_out.getvalue(),
                             "** instance id missing **\n")
