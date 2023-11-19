#!/usr/bin/python3
"""
Defines the Review class.
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Represents a review and inherits from the BaseModel class.
    """

    place_id = ""
    user_id = ""
    text = ""
