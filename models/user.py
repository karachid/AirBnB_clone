#!/usr/bin/python3
"""Defines a User class"""
from models.base_model import BaseModel


class User(BaseModel):
    """Declares User class """

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """initialize variables and methods of User"""
        super().__init__(self, *args, **kwargs)
        if kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "email":
                    self.email = v
                elif k == "password":
                    self.password = v
                elif k == "first_name":
                    self.first_name = v
                elif k == "last_name":
                    self.last_name = v
