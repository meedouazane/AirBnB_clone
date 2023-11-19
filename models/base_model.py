#!/usr/bin/env python3
"""
Defines the BaseModel class.
"""
from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """
    Defines common attributes/methods for other classes.

    Attributes:
        id (string): A unique id generated using uuid4.
        created_at (datetime): The time when the instance is created.
        updated_at (datetime): The time of the last instance's update.
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize a BaseModel instance.

        Args:
            *args: Unused variable length argument list.
            **kwargs: Keyword arguments for attributes.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                if key in ["created_at", "updated_at"]:
                    value = datetime.fromisoformat(value)
                setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def save(self):
        """Update the 'updated_At' attribute to the current time."""
        self.updated_at = datetime.now()
        models.storage.save()

    def __str__(self):
        """Return the string representation of the BaseModel instance."""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def to_dict(self):
        """Return a dictionary containing all keys/values
        of __dict__ of the instance."""
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__
        new_dict["created_at"] = datetime.isoformat(self.created_at)
        new_dict["updated_at"] = datetime.isoformat(self.updated_at)
        return new_dict
