#!/usr/bin/python3
"""
Init file of the models package
"""
from .engine import file_storage
from models.base_model import BaseModel
from models.user import User

storage = file_storage.FileStorage()
storage.reload()
