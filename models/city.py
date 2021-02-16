#!/usr/bin/python3
""" This module defines City object in our HBnB """
from models.base_model import BaseModel


class City(BaseModel):
    """ City class
        Based on BaseModel
    """
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
