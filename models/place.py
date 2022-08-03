#!/usr/bin/env python3
"""module place for Airbnb clone"""
from base_model import BaseModel as base


class Place(base):
    """
    class place containing
    """
    name = ""
    city_id = ""
    user_id = ""
    description = ""
    number_of_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
