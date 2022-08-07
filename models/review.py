#!/usr/bin/env python3
"""reviews model"""

from models.base_model import BaseModel as base


class Reviews(base):
    """defines reviews class"""
    place_id = ""
    user_id = ""
    text = ""
