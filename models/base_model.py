#!/usr/bin/python3
# Public instance attributes
'''
    class Base Model
'''
from datetime import datetime
import models
import uuid


class BaseModel():
    '''
        BaseModel definition
    '''

    id = ''
    created_at = datetime.now()
    updated_at = datetime.now()

    def __init__(self, *args, **kwargs):
        '''
            initialise values
            Re-created an instance with
            dictionary representation
        '''
        format = '%Y-%m-%dT%H:%M:%S.%f'
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ['created_at', 'updated_at']:
                        value = datetime.strptime(value, format)
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            '''
                create a unique FileStorage instance
                for your application
            '''
            models.storage.new(self)

    def __str__(self):
        '''
            Return:
                class name
                class id
                class dictionary
        '''
        return ("[{}] ({}) {}".format(type(self).__name__,
                self.id, self.__dict__))

    '''
        Public instance methods
    '''
    def save(self):
        '''
            updates the public instances attrib. update_at
            with cuyrrent datetime
        '''
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        '''
            Return:
                dictionary containing keys/values
                of __dict__ of instance
        '''
        my_dict = dict(self.__dict__)
        my_dict['__class__'] = self.__class__.__name__
        my_dict['created_at'] = self.created_at.isoformat()
        my_dict['updated_at'] = self.updated_at.isoformat()
        return my_dict
