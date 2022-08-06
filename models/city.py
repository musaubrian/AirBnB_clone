#!/usr/bin/env python3
"""module for the city"""

from models.base_model import BaseModel as base


class City(base):
    """city class containing state id and name"""
    name = ""
    state_id = ""
