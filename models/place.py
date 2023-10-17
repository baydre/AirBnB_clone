#!/usr/bin/python3
'''
    the Place class Model
'''
from models.base_model import BaseModel
# from models.city import City


class Place(BaseModel):
    '''
        defines the Place class model
    '''
    city_id = ''
    user_id = ''
    name = ''
    description = ''
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    '''
    def __init__(self):
        ''
        ''
        self.city_id = City.id
        self.user_id = User.id
    '''
