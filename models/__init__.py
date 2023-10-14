#!/usr/bin/python3
'''
    init - Python Package
'''
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

classes = {'BaseModel': BaseModel}

storage = FileStorage()
storage.reload()
