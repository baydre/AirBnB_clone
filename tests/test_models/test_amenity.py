#!/usr/bin/python3
'''
Module
'''
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    '''
    Docs
    '''

    def test_moduleDocs(self):
        '''
        Docs
        '''
        moduleDoc = (
                __import__("models.amenity")
                .amenity.__doc__)
        self.assertGreater(len(moduleDoc), 0)

    def test_classDocs(self):
        '''
        Docs
        '''
        classDoc = (
                __import__("models.amenity")
                .amenity.Amenity.__doc__)
        self.assertGreater(len(classDoc), 0)

    def test_name_Type(self):
        '''
        Docs
        '''
        amenity = Amenity()
        self.assertIs(type(amenity.name), str)


if __name__ == "__main__":
    unittest.main()
