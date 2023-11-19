#!/usr/bin/python3
''' city class that inherit from BaseModel '''
from models.base_model import BaseModel


class City(BaseModel):
    ''' city class that inherit from BaseModel '''

    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        ''' Initializition. '''
        super().__init__(*args, **kwargs)
