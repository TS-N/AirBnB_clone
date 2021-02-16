#!/usr/bin/python3
""" This module defines Review object in our HBnB """
from models.base_model import BaseModel


class Review(BaseModel):
    """ Review class
        Based on BaseModel
    """
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
