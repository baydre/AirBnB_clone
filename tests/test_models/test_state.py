#!/usr/bin/python3
'''
Module
'''
import unittest
from models.state import State


class TestState(unittest.TestCase):
    '''
    Docs
    '''

    def test_moduleDocs(self):
        '''
        Docs
        '''
        moduleDoc = (
                __import__("models.state")
                .state.__doc__)
        self.assertGreater(len(moduleDoc), 0)

    def test_classDocs(self):
        '''
        Docs
        '''
        classDoc = (
                __import__("models.state")
                .state.State.__doc__)
        self.assertGreater(len(classDoc), 0)

    def test_name_Type(self):
        '''
        Docs
        '''
        state = State()
        self.assertIs(type(state.name), str)


if __name__ == "__main__":
    unittest.main()
