#!/usr/bin/python3
"""Defines a Place class"""
from models.base_model import BaseModel


class Place(BaseModel):
    """Declares User class """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    def __init__(self, *args, **kwargs):
        """initialize variables and methods of User"""
        super().__init__(self, *args, **kwargs)
        if kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "city_id":
                    self.city_id = v
                elif k == "user_id":
                    self.password = v
                elif k == "name":
                    self.name = v
                elif k == "description":
                    self.description = v
                elif k == "number_rooms":
                    self.number_rooms = v
                elif k == "number_bathrooms":
                    self.number_bathrooms = v
                elif k == "max_guest":
                    self.max_guest = v
                elif k == "price_by_night":
                    self.price_by_night = v
                elif k == "latitude":
                    self.latitude = v
                elif k == "longitude":
                    self.longitude = v
                elif k == "amenity_id":
                    self.amenity_ids = v
