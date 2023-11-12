#!/usr/bin/python3
"""Defines Amenity class"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """ Declares Amenity class  """

    name = ""
    '''
    def __init__(self, *args, **kwargs):
        """initialize variables of Amenity"""
        super().__init__(self, *args, **kwargs)
        if kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "name":
                    self.name = v
    '''
