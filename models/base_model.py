#!/usr/bin/env python3
"""base class model to be inherited by other classes"""

from uuid import uuid4
from datetime import datetime
import json


class BaseModel:
    """
    defines base model class
    """

    def __init__(self, *args, **kwargs) -> None:
        """instatiate base_class"""

        if len(kwargs) == 0:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            kwargs["created_at"] = datetime.strptime(
                    kwargs["created_at"],
                    "%Y-%m-%dT%H:%M:%S.%f"
                    )
            kwargs["updated_at"] = datetime.strptime(
                    kwargs["updated_at"],
                    "%Y-%m-%dT%H:%M:%S.%f"
                    )
            for k, v in kwargs.items():
                if "__class__" not in k:
                    setattr(self, k, v)

    def __str__(self):
        """
        return string representation of the class
        """
        return (
                f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
                )
