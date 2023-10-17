#!/usr/bin/python3
'''
    Recreate BaseModel from another one using dict. repr.
'''
import models
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.City import city
from models.amenity import Amenity
from models.review import Review
import json
from os.path import isfile


class FileStorage:
    ''' defines The file storage class'''
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        '''
            Returns/displays dict objects
        '''
        return self.__objects

    def new(self, obj):
        '''
            sets new objects to dictionary
        '''
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        if key:
            self.__objects[key] = obj

    def save(self):
        '''
            serialization of __objects to JSON file
        '''
        serialised_objects = {}
        '''
        for key, obj in FileStorage.__objects.items():
            serialised_objects[key] = obj.to_dict()
        '''
        with open(self.__file_path, 'w+') as file:
            for key, obj in self.__objects.items():
                '''
                Assign a key-value pair to the serialized_objects dictionary.
                The key is the same as the key from __objects, and
                the obj is obtained by calling the to_dict() method
                    on the obj object.
                Assume that each object (obj) has a method called to_dict()
                that returns a dictioonary represemtation of the object.

                Take each object in the __objects dictionary,
                Convert it into a dictionary representation using the
                    `to_dict()` method.
                '''
                serialised_objects[key] = obj.to_dict()
            json.dump(serialised_objects, file)

    def reload(self):
        '''
            This Deserializes saved objects stored in the JSON file
            to __objects
        '''
        try:
            if isfile(self.__file_path):
                ''' Open file and commit deserialization '''
                with open(self.__file_path, 'r+') as file:
                    data = json.load(file)
                    for key, obj_dict in data.items():
                        '''
                            using the **keyword argument comcept
                            to retrieve obj from json file
                        '''
                        class_name = obj_dict['__class__']
                        # del obj_dict['__class__']
                        # obj_instance = eval(class_name)(**obj_dict)
                        '''
                            Updated to correctly serialize and
                            deserialize User
                        '''
                        obj_dict = eval(class_name)(**obj_dict)
                        self.__objects[key] = obj_dict
        except FileNotFoundError:
            '''
                if file does not exist
            '''
            pass
