#!/usr/bin/python3
"""
Unit tests for the BaseModel class.
"""
import unittest
from models.base_model import BaseModel
from models.place import Place


class TestPlace(unittest.TestCase):
    ''' test place '''

    def testname(self):
        ''' test first name'''
        Place.name = "Messi"
        self.assertEqual(Place.name, "Messi")

    def testnameEmpty(self):
        ''' test first name empty '''
        Place.name = ""
        self.assertEqual(Place.name, "")

    def testUser_id(self):
        ''' test first name'''
        Place.user_id = "1x22"
        self.assertEqual(Place.user_id, "1x22")

    def testUser_idEmpty(self):
        ''' test first name empty '''
        Place.user_id = ""
        self.assertEqual(Place.user_id, "")

    def testcity_id(self):
        ''' test first name'''
        Place.city_id = "1x22"
        self.assertEqual(Place.city_id, "1x22")

    def testUser_idEmpty(self):
        ''' test first name empty '''
        Place.city_id = ""
        self.assertEqual(Place.city_id, "")

    def testdescription(self):
        ''' test description'''
        Place.description = "hello this is description"
        self.assertEqual(Place.description, "hello this is description")

    def testDescriptionEmpty(self):
        ''' test description empty '''
        Place.description = ""
        self.assertEqual(Place.description, "")

    def testnumber_rooms(self):
        ''' test number_rooms'''
        Place.number_rooms = 5
        self.assertEqual(Place.number_rooms, 5)

    def testnumber_bathrooms(self):
        ''' test description'''
        Place.number_bathrooms = 3
        self.assertEqual(Place.number_bathrooms, 3)

    def testmax_guest(self):
        ''' test max_guest '''
        Place.max_guest = 20
        self.assertEqual(Place.max_guest, 20)

    def testprice_by_night(self):
        ''' test price_by_night '''
        Place.price_by_night = 30
        self.assertEqual(Place.price_by_night, 30)

    def testlatitude(self):
        ''' test latitude '''
        Place.latitude = 0.30
        self.assertEqual(Place.latitude, 0.30)

    def testlatitude(self):
        ''' test longitude '''
        Place.longitude = 0.30
        self.assertEqual(Place.longitude, 0.30)

    def testamenity_ids(self):
        ''' test longitude '''
        Place.amenity_ids = ["ab", "ac"]
        self.assertEqual(Place.amenity_ids, ['ab', 'ac'])
