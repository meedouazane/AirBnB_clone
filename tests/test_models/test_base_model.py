#!/usr/bin/python3
"""
Unit tests for the BaseModel class.
"""
import unittest
from models.base_model import BaseModel
import uuid
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """
    Test cases for BaseModel class.
    """

    def setUp(self):
        """Create a BaseModel to use in tests."""
        self.base = BaseModel()

    def create_instance_from_kwargs(self):
        """
        Helper function for 'kwargs' test cases.

        Returns:
            BaseModel: A BaseModel instance created using 'kwargs'.
        """
        base_json = {
            "id": "836f35d9-6bd9-4223-a8c5-b15fcb27f037",
            "created_at": "2023-11-08T12:24:58.970629",
            "updated_at": "2023-11-08T12:24:58.970634",
            "name": "First_Model",
            "number": 89,
        }
        return BaseModel(**base_json)

    def test_instance_creation(self):
        """Assert the instance created in the'setUp' method
        is an instance of BaseModel."""
        self.assertIsInstance(self.base, BaseModel)

    def test_objects_inequality(self):
        """Check the inequality of two created instances."""
        base2 = BaseModel()
        self.assertNotEqual(self.base, base2)

    def test_instance_has_id(self):
        """Check that a newly created instance has an 'id' attribute."""
        self.base = BaseModel()
        self.assertTrue(hasattr(self.base, "id"))

    def test_id_is_string(self):
        """Ensure the 'id' attribute is a string."""
        self.assertIsInstance(self.base.id, str)

    def test_id_is_uuid4(self):
        """Verify that the 'id' attribute follows the UUID4 format."""
        uuid_obj = uuid.UUID(self.base.id)
        self.assertEqual(uuid_obj.version, 4)

    def test_id_is_unique(self):
        """Ensure the 'id' of each instance is unique."""
        base2 = BaseModel()
        self.assertNotEqual(self.base.id, base2.id)

    def test_instance_has_created_at(self):
        """Check that a newly created instance
        has 'created_at' attribute."""
        self.assertTrue(hasattr(self.base, "created_at"))

    def test_instance_has_updated_at(self):
        """Check that a newly created instance
        has 'updated_at' attribute."""
        self.assertTrue(hasattr(self.base, "updated_at"))

    def test_created_at_is_datetime(self):
        """Ensure the 'created_at' attribute is a datetime."""
        self.assertIsInstance(self.base.created_at, datetime)

    def test_updated_at_is_datetime(self):
        """Ensure the 'updated_at' attribute is a datetime."""
        self.assertIsInstance(self.base.updated_at, datetime)

    def test_updated_at_comes_after_created_at(self):
        """Check that 'updated_at' attrbiute
        comes after 'create_at' attribute."""
        self.assertGreater(self.base.updated_at, self.base.created_at)

    def test_str_method_format(self):
        """Check the '__str__' method format."""
        self.base.name = "First Model"
        self.base.number = 89
        expected = f"[BaseModel] ({self.base.id}) {self.base.__dict__}"
        self.assertEqual(str(self.base), expected)

    def test_has_save_method(self):
        """Check if created BaseModel instance has a 'save' method."""
        self.assertTrue(hasattr(self.base, "save"))

    def test_save_sets_updated_at_to_current_time(self):
        """Verify that the 'save' method sets the 'updated_at'
        attribute to the current time."""
        current = datetime.now()
        self.base.save()
        diff = (self.base.updated_at - current).total_seconds()
        self.assertLess(diff, 1)

    def test_has_to_dict_method(self):
        """Check if created BaseModel instance has a 'to_dict' method."""
        self.assertTrue(hasattr(self.base, "to_dict"))

    def test_to_dict_output(self):
        """Check the output of the 'to_dict' method."""
        self.base.name = "First Model"
        self.base.number = 89
        expected_dict = {
            "id": self.base.id,
            "created_at": datetime.isoformat(self.base.created_at),
            "updated_at": datetime.isoformat(self.base.updated_at),
            "name": self.base.name,
            "number": self.base.number,
            "__class__": self.base.__class__.__name__,
        }
        self.assertEqual(self.base.to_dict(), expected_dict)

    def test_created_at_not_changed(self):
        """Ensure that 'created_at' attribute is not changed
        when calling 'to_dict'."""
        original = self.base.created_at
        self.base.to_dict()
        self.assertEqual(self.base.created_at, original)

    def test_updated_at_not_changed(self):
        """Ensure that 'updated_at' attribute is not changed
        when calling 'to_dict'."""
        original = self.base.updated_at
        self.base.to_dict()
        self.assertEqual(self.base.updated_at, original)

    def test_instance_is_BaseModel_if_kwargs(self):
        """Check if the instance is created using 'kwrags',
        if it's not empty."""
        base = self.create_instance_from_kwargs()
        self.assertIsInstance(base, BaseModel)

    def test_id_is_from_kwargs(self):
        """Check if the 'id' attribute is created from 'kwargs'."""
        base = self.create_instance_from_kwargs()
        self.assertEqual(base.id, "836f35d9-6bd9-4223-a8c5-b15fcb27f037")

    def test_created_at_from_kwargs_is_datetime(self):
        """Check if the 'created_at' attribute is a datetime object."""
        base = self.create_instance_from_kwargs()
        self.assertIsInstance(base.created_at, datetime)

    def test_updated_at_from_kwargs_is_datetime(self):
        """Check if the 'updated_at' attribute is a datetime object."""
        base = self.create_instance_from_kwargs()
        self.assertIsInstance(base.updated_at, datetime)

    def test_created_at_is_from_kwargs(self):
        """Check if the 'created_at' attribute is created from 'kwargs'."""
        base = self.create_instance_from_kwargs()
        self.assertEqual(
            base.created_at,
            datetime.fromisoformat("2023-11-08T12:24:58.970629"),
        )

    def test_updated_at_is_from_kwargs(self):
        """Check if the 'updated_at' attribute is created from 'kwargs'."""
        base = self.create_instance_from_kwargs()
        self.assertEqual(
            base.updated_at,
            datetime.fromisoformat("2023-11-08T12:24:58.970634"),
        )

    def test_name_is_from_kwargs(self):
        """Check if the 'name' attribute is created from 'kwargs'."""
        base = self.create_instance_from_kwargs()
        self.assertEqual(base.name, "First_Model")

    def test_number_is_from_kwargs(self):
        """Check if the 'number' attribute is created from 'kwargs'."""
        base = self.create_instance_from_kwargs()
        self.assertEqual(base.number, 89)
