#!/usr/bin/env python3
"""file stroage module"""

import json


class FileStorage:
    """
    defines a file storage class
    """

    __path = "file_storage.json"
    __objects = {}

    def all(self):
        """
        return all __objects
        """
        return self.__objects

    def new(self, obj):
        """
        create new __object instance
        args:
            obj: instance object
        """
        
        k = f"{obj.__class__.__name__}.{obj.id}"
        v = obj
        FileStorage.__objects[k] = v

    def save(self):
        """
        saves to json file
        """
        objects_dict = {}
        for k, v in FileStorage.__objects.items():
            objects_dict[k] = v.to_dict()

        with open(FileStorage.__path, "w") as file:
            json.dump(objects_dict, file)
