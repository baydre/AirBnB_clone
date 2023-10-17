#!/usr/bin/python3

'''
    Unit tests for file storage.
'''

from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from os import path, remove
import io
import json
import unittest
import models


class Test_all(unittest.TestCase):
    '''
        Test:
            all command.
    '''

    def set_up(self):
        '''
            Test:
                Sets up test
        '''
        try:
            remove("file.json")
        except FileNotFoundError:
            pass
        FileStorage._FileStorage__objects = {}

    def tear_down(self):
        '''
            Test:
                Tears down the tests.
        '''
        try:
            remove("file.json")
        except FileNotFoundError:
            pass

    def test_all_without_arg(self):
        '''
            Tests:
                all command without arguments.
        '''
        self.assertEqual(models.storage.all(), {})

    def test_all_with_arg(self):
        '''
            Test:
                all command with arguments.
        '''
        baseM = BaseModel()
        name = baseM.__class__.__name__ + '.' + baseM.id
        dict_ = {name: baseM}
        self.assertEqual(models.storage.all(), {})

    def test_all_classes(self):
        '''
            Tests the.
        '''
        basem = BaseModel()

        dicts = models.storage.all()
        self.assertEqual(baseM, dicts['BaseModel.{}'.format(baseM.id)])
