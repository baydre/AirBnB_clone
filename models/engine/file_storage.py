#!/usr/bin/python3
'''
    Recreate BaseModel from another one using dict. repr.
'''

import json
from models.base_model import BaseModel
from os.path import isfile


class FileStorage:
    ''' defines The file storage class'''
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        ''' displays dict objects '''
        return FileStorage.__objects

    def new(self, obj):
        ''' '''
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        ''' '''
        serialised_objects = {}
        for key, obj in FileStorage.__objects.items():
            serialised_objects[key] = obj.to_dict()
        with open(FileStorage.__file_path, 'w') as file:
            json.dump(serialised_objects, file)

    def reload(self):
        ''' '''
        if isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r') as file:
                data = json.load(file)
                for key, obj_dict in data.items():
                    class_name = obj_dict['__class__']
                    del obj_dict['__class__']
                    obj_instance = eval(class_name)(**obj_dict)
                    FileStorage.__objects[key] = obj_instance
