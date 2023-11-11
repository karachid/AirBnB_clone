#!/usr/bin/python3
"""Defines a Review class"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Declares User class """

    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """initialize variables and methods of User"""
        super().__init__(self, *args, **kwargs)
        if kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "place_id":
                    self.place_id = v
                elif k == "user_id":
                    self.user_id = v
                elif k == "text":
                    self.text = v
