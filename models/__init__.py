#!/usr/bin/env python3
"""
initialize package
"""

from models.engine.file_storage import FileStorage
from models.amenity import Amenity
from models.base_model import BaseModel as base
from models.city import City
from models.place import Place
from models.review import Reviews
from models.state import State
from models.user import User


my_classes = {
        "Amenity": Amenity, "BaseModel": base,
        "City": City, "Place": Place,
        "Reviews": Reviews, "State": State,
        "User": User
        }

storage = FileStorage()
storage.reload()
