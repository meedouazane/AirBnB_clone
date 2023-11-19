#!/usr/bin/python3
"""
Unit tests for the State class.
"""
import unittest
from models.base_model import BaseModel
import uuid
from datetime import datetime
from models.state import State


class TestState(unittest.TestCase):
    """
    Test cases for State class.
    """
    def testname(self):
        ''' test first name'''
        State.name = "Messi"
        self.assertEqual(State.name, "Messi")

    def testnameEmpty(self):
        ''' test first name empty '''
        State.name = ""
        self.assertEqual(State.name, "")
