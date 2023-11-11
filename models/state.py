#!/usr/bin/python3
"""Defines a State class"""
from models.base_model import BaseModel


class State(BaseModel):
    """ Declares State class """

    name = ""

    def __init__(self, *args, **kwargs):
        """ Initializes variables of State """
        super().__init__(self, *args, **kwargs)
        if kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "name":
                    self.name = v
