#!/usr/bin/python3
"""
Init file of the models package
"""
from .engine import file_storage


storage = file_storage.FileStorage()
storage.reload()
