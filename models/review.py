#!/usr/bin/python3
'''
    the review class model
'''
from models.base_model import BaseModel
from models.place import Place
from models.user import User


class Review(BaseModel):
    '''
        define the Review class
    '''


    def __init__(self, *args, **kwargs):
        '''
            method
        '''
        self.place_id = Place.id
        self.user_id = User.id
        self.test = ''
