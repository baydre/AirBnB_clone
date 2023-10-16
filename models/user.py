#!/usr/bin/python3
'''
    A class User that inherits from BaseModel
'''
from models.base_model import BaseModel


class User(BaseModel):
    '''
        defines the User class
    '''

    def __init__(self, *args, **kwargs):
        '''
            defined the public class attrib;
                to be  called when a new instance of
                the class User is created.
        '''
        super().__init__(*args, **kwargs)

        self.email = ''
        self.password = ''
        self.first_name = ''
        self.last_name = ''
