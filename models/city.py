#!/usr/bin/python3
"""Defines a City class"""
from models.base_model import BaseModel


class City(BaseModel):
    """ Declares City class """

    state_id = ""
    name = ""
    '''
    def __init__(self, *args, **kwargs):
        """ Initializes variables of City """
        super().__init__(self, *args, **kwargs)
        if kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "state_id":
                    self.state_id = v
                elif k == "name":
                    self.name = v
    '''
