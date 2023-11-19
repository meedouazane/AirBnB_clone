#!/usr/bin/python3
''' amenity class that inherit from BaseModel '''
from models.base_model import BaseModel


class Amenity(BaseModel):
    ''' Amenity class that inherit from BaseModel '''

    name = ""

    def __init__(self, *args, **kwargs):
        ''' Initializition. '''
        super().__init__(*args, **kwargs)
