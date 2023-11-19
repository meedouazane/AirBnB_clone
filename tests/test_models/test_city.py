#!/usr/bin/python3
"""
Unit tests for the BaseModel class.
"""
import unittest
from models.base_model import BaseModel
from models.city import City


class TestCity(unittest.TestCase):
    ''' test city user '''

    def testname(self):
        ''' test first name'''
        City.name = "Messi"
        self.assertEqual(City.name, "Messi")

    def testnameEmpty(self):
        ''' test first name empty '''
        City.name = ""
        self.assertEqual(City.name, "")

    def testState_id(self):
        ''' test first name'''
        City.state_id = "Messi"
        self.assertEqual(City.state_id, "Messi")

    def testState_idEmpty(self):
        ''' test first name empty '''
        City.State_id = ""
        self.assertEqual(City.State_id, "")
