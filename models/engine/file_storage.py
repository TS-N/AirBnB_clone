#!/usr/bin/python3
"""
This module will take care of the
	serialization/deserialization
	storage on file
	in JSON
of our objects
"""
import json
from models.base_model import BaseModel
from models.user import User

class FileStorage:
	"""
	Class used to manage data storage
		__file_path: string - path to the JSON file
		__objects: dictionary will store all objects by <class name>.id
	"""
	__file_path = "file.json"
	__objects = {}

	def all(self):
		""" returns the dictionary __objects """
		return self.__objects

	def new(self, obj):
		""" sets in __objects the obj """
		self.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

	def save(self):
		""" serializes __objects to the JSON file """
		with open(self.__file_path, "w") as f:
			dic = {}
			for key, value in self.__objects.items():
				dic[key] = value.to_dict()
			f.write(json.dumps(dic))

	def reload(self):
		""" deserializes the JSON file to __objects """
		try:
			with open(self.__file_path, "r") as f:
				d = json.loads(f.read())
				for key, value in d.items():
					self.__objects[key] = BaseModel(**value)
		except:
			pass
