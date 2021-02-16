#!/usr/bin/python3
""" This module defines User object in our HBnB """
from models.base_model import BaseModel


class User(BaseModel):
    """ User class
        Based on BaseModel
    """"
    email = ""
    password = ""
    first_name = ""
    last_name = ""
