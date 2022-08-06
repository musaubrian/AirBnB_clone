#!/usr/bin/env python3
"""user module"""


from models.base_model import BaseModel as base


class User(base):
    """
    defines class user
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
