#!/usr/bin/python3
"""
Base model class that defines all common attributes/methods for other classes
"""
from datetime import datetime
import uuid
import models


class BaseModel:
    """ BaseModel for HBnB
        Can interact with the storage
        Can be called from console
    """
    def __init__(self, *args, **kwargs):
        if kwargs != {}:
            for k in kwargs:
                if k != "__class__":
                    if k != "created_at" and k != "updated_at":
                        setattr(self, k, kwargs[k])
                    else:
                        dt = "%Y-%m-%dT%H:%M:%S.%f"
                        setattr(self, k, datetime.strptime(kwargs[k], dt))
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        return "[{}] ({}) {}".format(
            self.__class__.__name__,
            self.id, self.__dict__)

    def save(self):
        """ updates the public instance attribute and saves state """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ generate a dictionary representation of the instance """
        d = {}
        for key, value in self.__dict__.items():
            if isinstance(value, datetime):
                d[key] = value.isoformat()
            else:
                d[key] = str(value)
        d["__class__"] = self.__class__.__name__
        return d
