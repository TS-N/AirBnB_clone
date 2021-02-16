#!/usr/bin/python3
""" This module defines State object in our HBnB """
from models.base_model import BaseModel


class State(BaseModel):
    """ State class
        Based on BaseModel
    """
    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
