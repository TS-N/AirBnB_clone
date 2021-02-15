#!/usr/bin/python3
"""Base model class that defines all common attributes/methods for other classes """
import datetime
import uuid
import models

class BaseModel:

    def __init__(self, *args, **kwargs):
        if kwargs != {}:
            for key in kwargs:
                if key != "__class__":
                    if key != "created_at" and key != "updated_at":
                        setattr(self, key, kwargs[key])
                    else:
                        setattr(self, key, datetime.datetime.strptime(kwargs[key], "%Y-%m-%dT%H:%M:%S.%f"))
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            models.storage.new(self)


    def __str__(self):
         return "[BaseModel] ({}) {}".format(self.id, self.__dict__)

    def save(self):
        """ updates the public instance attribute and saves state """
        self.updated_at = datetime.datetime.now()
        models.storage.save()

    def to_dict(self):
        """ generate a dictionary representation of the instance """
        d = {}
        for key, value in self.__dict__.items():
            if isinstance(value, datetime.datetime):
                d[key] = value.isoformat()
            else:
                d[key] = str(value)
        d["__class__"] = self.__class__.__name__
        return d

