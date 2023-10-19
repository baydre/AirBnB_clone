#!/usr/bin/python3
import unittest
from models import storage, FileStorage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
import os

class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.storage = FileStorage()

    def tearDown(self):
        if os.path.exists(self.storage._FileStorage__file_path):
            os.remove(self.storage._FileStorage__file_path)

    def test_new(self):
        new_model = BaseModel()
        self.storage.new(new_model)
        self.assertIn('BaseModel.' + new_model.id, self.storage.all())

    def test_all(self):
        all_objects = self.storage.all()
        self.assertIsInstance(all_objects, dict)

    def test_save_reload(self):
        new_model = BaseModel()
        self.storage.new(new_model)
        self.storage.save()
        loaded_storage = FileStorage()
        loaded_storage.reload()
        loaded_objects = loaded_storage.all()
        self.assertIn('BaseModel.' + new_model.id, loaded_objects)

if __name__ == '__main__':
    unittest.main()
