#!/usr/bin/python3
# Public instance attributes
'''
class Base Model
'''
import uuid
from datetime import datetime
import models

class BaseModel():
    '''
    BaseModel definition
    '''

    id = ''
    created_at = None
    updated_at = None

    def __init__(self, *args, **kwargs):
        '''
        initialise values
        '''
# Re-created an instance with dictionary representation
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
            # create a unique FileStorage instance for your application
            models.storage.new(self)

    def __str__(self):
        return ("[{}] ({}) {}".format(type(self).__name__,
                self.id, self.__dict__))

# Public instance methods
    def save(self):
        ''' Comment '''
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        ''' Comment '''
        mydict = {}
        for key, value in self.__dict__.items():
            if isinstance(value, datetime):
                mydict[key] = value.isoformat()
            else:
                mydict[key] = value
        return {
                **mydict,
                '__class__': type(self).__name__
                }
