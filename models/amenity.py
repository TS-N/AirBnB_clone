#!/usr/bin/python3
""" This module defines Ameity object in our HBnB """
from models.base_model import BaseModel


class Amenity(BaseModel):
    """ Amenity class
        Based on BaseModel
    """
    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
