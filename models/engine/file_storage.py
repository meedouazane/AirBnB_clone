#!/usr/bin/python3
"""
Defines the FileStorage class.
"""

from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import json

classes = {
    "BaseModel": BaseModel,
    "Amenity": Amenity,
    "City": City,
    "Place": Place,
    "Review": Review,
    "State": State,
    "User": User,
}


class FileStorage:
    """
    Serializes instances to a JSON file and deserialize JSON file to instances.

    Attributes:
        __file_path (str): Path to the JSON file.
        __objects (dict): Dictionary to store all objects.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary of objects."""
        return self.__objects

    def new(self, obj):
        """Set in '__objects' the 'obj' with key '<obj class name>.id'."""
        if obj:
            key = f"{obj.__class__.__name__}.{obj.id}"
            self.__objects[key] = obj

    def save(self):
        """Serialize '__objects' to the JSON file in '__file_path'."""
        with open(self.__file_path, "w", encoding="utf-8") as file:
            obj_dict = {}
            for key, value in self.__objects.items():
                obj_dict[key] = value.to_dict()
            json.dump(obj_dict, file, indent=4)

    def reload(self):
        """Deserialize the JSON file in '__file_path' to '__objects'."""
        try:
            with open(self.__file_path, "r", encoding="utf-8") as file:
                json_dict = json.load(file)
                for key, value in json_dict.items():
                    cls_name = key.split(".")[0]
                    cls = classes[cls_name]
                    obj = cls(**value)
                    self.new(obj)
        except Exception:
            return
