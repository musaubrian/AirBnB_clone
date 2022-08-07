#!/usr/bin/env python3
"""user module for the Airbnb project"""
from models.base_model import BaseModel as base


class Amenity(base):
    """defines amenity class inheriting class base"""
    name = ""
