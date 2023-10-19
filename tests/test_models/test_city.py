#!/usr/bin/python3
'''
Module
'''
import unittest
from models.city import City


class TestCity(unittest.TestCase):
    '''
    Docs
    '''

    def test_moduleDocs(self):
        '''
        Docs
        '''
        moduleDoc = (
                __import__("models.city")
                .city.__doc__)
        self.assertGreater(len(moduleDoc), 0)

    def test_classDocs(self):
        '''
        Docs
        '''
        classDoc = (
                __import__("models.city")
                .city.City.__doc__)
        self.assertGreater(len(classDoc), 0)

    def test_name_Type(self):
        '''
        Docs
        '''
        city = City()
        self.assertIs(type(city.name), str)

    def test_state_id_Type(self):
        '''
        Docs
        '''
        city = City()
        self.assertIs(type(city.state_id), str)


if __name__ == "__main__":
    unittest.main()
