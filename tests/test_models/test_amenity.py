#!/usr/bin/python3
"""
Unit tests for the Amenity class.
"""
import unittest
from models.base_model import BaseModel
import uuid
from datetime import datetime
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """
    Test cases for Amenity class.
    """
    def testname(self):
        ''' test first name'''
        Amenity.name = "Messi"
        self.assertEqual(Amenity.name, "Messi")

    def testnameEmpty(self):
        ''' test first name empty '''
        Amenity.name = ""
        self.assertEqual(Amenity.name, "")
