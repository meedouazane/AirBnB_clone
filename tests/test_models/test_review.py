#!/usr/bin/python3
"""
Unit tests for the Review class.
"""
import unittest
from models.base_model import BaseModel
import uuid
from datetime import datetime
from models.review import Review


class TestReview(unittest.TestCase):
    """
    Test cases for Review class.
    """
    def testplace_id(self):
        ''' test place_id'''
        Review.place_id = "1b12"
        self.assertEqual(Review.place_id, "1b12")

    def testplace_idEmpty(self):
        ''' test place_id empty '''
        Review.place_id = ""
        self.assertEqual(Review.place_id, "")

    def testplace_id(self):
        ''' test user_id'''
        Review.user_id = "1b12"
        self.assertEqual(Review.user_id, "1b12")

    def testplace_idEmpty(self):
        ''' test user_id empty '''
        Review.user_id = ""
        self.assertEqual(Review.user_id, "")

    def testtext(self):
        ''' test text'''
        Review.text = "hello world"
        self.assertEqual(Review.text, "hello world")

    def testtextEmpty(self):
        ''' test text empty '''
        Review.text = ""
        self.assertEqual(Review.text, "")
