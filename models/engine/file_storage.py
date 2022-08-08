#!/usr/bin/env python3
"""file storage module"""

import json
import models


class FileStorage:
    """
    defines a file storage class
    """

    __file_path = "file_storage.json"
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

        key = str(obj.__class__.__name__) + "." + str(obj.id)
        val = obj
        FileStorage.__objects[key] = val

    def save(self):
        """
        saves to json file
        """
        objects_dict = {}
        for k, v in FileStorage.__objects.items():
            objects_dict[k] = v.to_dict()

        with open(FileStorage.__file_path, "w", encoding="UTF8") as file:
            json.dump(objects_dict, file)

    def reload(self):
        """
        reads from the json file
        `deserializes` json file
        """
        try:
            with open(FileStorage.__file_path, encoding="UTF8") as file:
                FileStorage.__objects = json.load(file)
            for k, v in FileStorage.__objects.items():
                class_name = v["__class__"]
                class_name = models.my_classes[class_name]
                FileStorage.__objects[k] = class_name(**v)
        except FileNotFoundError:
            pass
