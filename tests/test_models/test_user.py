#!/usr/bin/python3
"""
Unit tests for the BaseModel class.
"""
import unittest
from models.base_model import BaseModel
from models.user import User


class TestUser(unittest.TestCase):
    ''' test class user '''

    def testEmail(self):
        ''' test email '''
        User.email = "mezane@yahoo.com"
        self.assertEqual(User.email, "mezane@yahoo.com")

    def testFirst_name(self):
        ''' test first name'''
        User.first_name = "Messi"
        self.assertEqual(User.first_name, "Messi")

    def testLast_name(self):
        ''' test last name '''
        User.last_name = "Lionel"
        self.assertEqual(User.last_name, "Lionel")

    def testPassword(self):
        ''' test password '''
        User.password = "@1a12s3Z"
        self.assertEqual(User.password, "@1a12s3Z")

    def testEmailEmpty(self):
        ''' test empty email '''
        User.email = ""
        self.assertEqual(User.email, "")

    def testFirst_nameEmpty(self):
        ''' test first name empty '''
        User.first_name = ""
        self.assertEqual(User.first_name, "")
