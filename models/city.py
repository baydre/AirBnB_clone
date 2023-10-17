#!/usr/bin/python3
'''
    The City class
'''
from models.base_model import BaseModel
# from models.state import State


class City(BaseModel):
    '''
        defines the City class
    '''
    state_id = ''
    name = ''
    
    '''
    def __init__(self, state_id, name):
        ''
            attributes: public method
        ''
        self.state_id = State.id
        self.name = ''
    '''
