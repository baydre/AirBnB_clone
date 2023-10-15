#!/usr/bin/python3
'''
Module
'''
import unittest
from unittest.mock import patch
from models.base_model import BaseModel
from uuid import UUID
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    '''
    Docs
    '''
    def test_moduleDocs(self):
        '''
        Docs
        '''
        moduleDoc = __import__("models.base_model").base_model.__doc__
        self.assertGreater(len(moduleDoc), 0)

    def test_classDocs(self):
        '''
        '''
        classDoc = __import__("models.base_model").base_model.BaseModel.__doc__
        self.assertGreater(len(classDoc), 0)

    def test_methodDocsSave(self):
        '''
        '''
        methodDoc = (
                __import__("models.base_model")
                .base_model.BaseModel.save.__doc__)
        self.assertGreater(len(methodDoc), 0)

    def test_methodDocsto_dict(self):
        '''
        '''
        methodDoc = (
                __import__("models.base_model")
                .base_model.BaseModel.to_dict.__doc__)
        self.assertGreater(len(methodDoc), 0)

    def test_methodDocs__str___(self):
        '''
        '''
        methodDoc = (
                __import__("models.base_model")
                .base_model.BaseModel.__str__.__doc__)
        self.assertGreater(len(methodDoc), 0)

    def test_idType(self):
        '''
        '''
        obj = BaseModel()
        self.assertIs(type(obj.id), str)

    def test_idLength(self):
        '''
        '''
        obj = BaseModel()
        self.assertEqual(len(obj.id), 36)

    def test_idValidity(self):
        '''
        '''
        obj = BaseModel()
        value = UUID(obj.id)
        self.assertIs(type(value), UUID)

    def test_created_atType(self):
        '''
        '''
        obj = BaseModel()
        self.assertIs(type(obj.created_at), datetime)

    def test_updated_atType(self):
        '''
        '''
        obj = BaseModel()
        self.assertIs(type(obj.updated_at), datetime)

    def test_outputOf__str__(self):
        '''
        '''
        obj = BaseModel()
        str1 = f"[BaseModel] ({obj.id}) {obj.__dict__}"
        str2 = str(obj)

        self.assertEqual(str1, str2)

    def test_updated_atChanged(self):
        '''
        '''
        obj = BaseModel()
        initial_value = obj.updated_at
        obj.save()

        self.assertGreater(obj.updated_at, initial_value)

    def test_to_dictCheck(self):
        '''
        '''
        obj = BaseModel()
        to_dict_dict = obj.to_dict()
        __dict__dict = obj.__dict__

        for keys in __dict__dict:
            self.assertIn(keys, to_dict_dict)

    def test_to_dict(self):
        '''
        '''
        obj = BaseModel()
        to_dict_dict = obj.to_dict()

        self.assertIn("__class__", to_dict_dict)
        self.assertIs(type(to_dict_dict["__class__"]), str)

    def test_to_dict_Valid(self):
        '''
        '''
        obj = BaseModel()
        to_dict_dict = obj.to_dict()
        created_at = datetime.fromisoformat(to_dict_dict["created_at"])
        updated_at = datetime.fromisoformat(to_dict_dict["updated_at"])

        self.assertIn("created_at", to_dict_dict)
        self.assertIn("updated_at", to_dict_dict)
        self.assertIs(type(to_dict_dict["created_at"]), str)
        self.assertIs(type(to_dict_dict["updated_at"]), str)
        self.assertEqual(to_dict_dict["created_at"], created_at.isoformat())
        self.assertEqual(to_dict_dict["updated_at"], updated_at.isoformat())

    def test_dictType(self):
        '''
        '''
        obj = BaseModel()
        to_dict_dict = obj.to_dict()

        self.assertIs(type(to_dict_dict["id"]), str)


if __name__ == "__main__":
    unittest.main()
