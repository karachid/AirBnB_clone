#!/usr/bin/python3
"""
Unittest for the BaseModel class
Test files by using the following command line:
python3 -m unittest tests/test_models/test_base_model.py
"""
import unittest
import pep8
from os import path, remove
import datetime
import models
from models import base_model
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestBaseModel(unittest.TestCase):
    """define variables and methods"""

    def setUp(self):
        """
        Method called to prepare the test fixture.
        It gets called immediately before calling the test method
        """
        FileStorage._FileStorage__objects = {}
        FileStorage._FileStorage__file_path = "file.json"

    def tearDown(self):
        """
        Deletes public FileStorage Props
        Method called immediately after the test method is called
        """
        del FileStorage._FileStorage__file_path
        del FileStorage._FileStorage__objects
        if path.exists("file.json"):
            remove("file.json")

    def test_pep8_conformance(self):
        """ Test that BaseModel conforms to PEP8 standards """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/base_model.py'])
        self.assertEqual(result.total_errors, 0, "Errors (and warnings).")

    def test_class_method_presence(self):
        """ Test that the BaseModel methods are defined """
        bs = dir(BaseModel)
        self.assertIn('__init__', bs)
        self.assertIn('save', bs)
        self.assertIn('to_dict', bs)
        self.assertIn('__str__', bs)

    def test_instance_method_presence(self):
        """Test that the BaseModel instance has the same methods"""
        bs = dir(BaseModel())
        self.assertIn('__init__', bs)
        self.assertIn('save', bs)
        self.assertIn('to_dict', bs)
        self.assertIn('__str__', bs)

    def test_instance_attribute_presence(self):
        """Test that the BaseModel instance attributes are declared"""
        bs = dir(BaseModel())
        self.assertIn('id', bs)
        self.assertIn('updated_at', bs)
        self.assertIn('created_at', bs)
        self.assertIn('__class__', bs)

    def test_docstring_presence(self):
        """Test that docstring is in Module, Class, and methods"""
        self.assertIsNot(base_model.__doc__, None)
        self.assertIsNot(BaseModel.__init__.__doc__, None)
        self.assertIsNot(BaseModel.save.__doc__, None)
        self.assertIsNot(BaseModel.to_dict.__doc__, None)
        self.assertIsNot(BaseModel.__str__.__doc__, None)

    def test_instantiation(self):
        """Test correct instantiation of object 'BaseModel()'"""

        bs = BaseModel()
        self.assertIsInstance(bs, BaseModel)
        self.assertIsInstance(bs.id, str)
        self.assertIsInstance(bs.created_at, datetime.datetime)
        self.assertIsInstance(bs.updated_at, datetime.datetime)
        self.assertIsInstance(bs.__class__, type)

        bs.size = "Short"
        l1 = dir(bs)
        self.assertIn('size', l1)
        self.assertEqual(bs.__dict__['size'], 'Short')

        bs.size = 'Short'
        l2 = dir(bs)
        self.assertIn('size', l2)
        self.assertEqual(bs.__dict__['size'], 'Short')

        bs.age = 32
        l3 = dir(bs)
        self.assertIn('age', l3)
        self.assertEqual(bs.__dict__['age'], 32)

        bs.age = 32.5
        l4 = dir(bs)
        self.assertIn('age', l4)
        self.assertEqual(bs.__dict__['age'], 32.5)

        bs.age = None
        l5 = dir(bs)
        self.assertIn('age', l5)
        self.assertEqual(bs.__dict__['age'], None)

        ba_kw1 = BaseModel(**{})
        self.assertIsInstance(ba_kw1, BaseModel)
        self.assertIsInstance(ba_kw1.id, str)
        self.assertIsInstance(ba_kw1.created_at, datetime.datetime)
        self.assertIsInstance(ba_kw1.updated_at, datetime.datetime)
        self.assertIsInstance(ba_kw1.__class__, type)

        ba_kw11 = BaseModel({})
        self.assertIsInstance(ba_kw11, BaseModel)
        self.assertIsInstance(ba_kw11.id, str)
        self.assertIsInstance(ba_kw11.created_at, datetime.datetime)
        self.assertIsInstance(ba_kw11.updated_at, datetime.datetime)
        self.assertIsInstance(ba_kw11.__class__, type)

        ba_kw12 = BaseModel([])
        self.assertIsInstance(ba_kw12, BaseModel)
        self.assertIsInstance(ba_kw12.id, str)
        self.assertIsInstance(ba_kw12.created_at, datetime.datetime)
        self.assertIsInstance(ba_kw12.updated_at, datetime.datetime)
        self.assertIsInstance(ba_kw12.__class__, type)

        ba_kw13 = BaseModel(())
        self.assertIsInstance(ba_kw13, BaseModel)
        self.assertIsInstance(ba_kw13.id, str)
        self.assertIsInstance(ba_kw13.created_at, datetime.datetime)
        self.assertIsInstance(ba_kw13.updated_at, datetime.datetime)
        self.assertIsInstance(ba_kw13.__class__, type)

        ba_kw14 = BaseModel(1)
        self.assertIsInstance(ba_kw14, BaseModel)
        self.assertIsInstance(ba_kw14.id, str)
        self.assertIsInstance(ba_kw14.created_at, datetime.datetime)
        self.assertIsInstance(ba_kw14.updated_at, datetime.datetime)
        self.assertIsInstance(ba_kw14.__class__, type)

        ba_kw15 = BaseModel("a")
        self.assertIsInstance(ba_kw15, BaseModel)
        self.assertIsInstance(ba_kw15.id, str)
        self.assertIsInstance(ba_kw15.created_at, datetime.datetime)
        self.assertIsInstance(ba_kw15.updated_at, datetime.datetime)
        self.assertIsInstance(ba_kw15.__class__, type)

        ba_kw16 = BaseModel(None)
        self.assertIsInstance(ba_kw16, BaseModel)
        self.assertIsInstance(ba_kw16.id, str)
        self.assertIsInstance(ba_kw16.created_at, datetime.datetime)
        self.assertIsInstance(ba_kw16.updated_at, datetime.datetime)
        self.assertIsInstance(ba_kw16.__class__, type)

        ba_kw17 = BaseModel({"first_name": "John"})
        self.assertIsInstance(ba_kw17, BaseModel)
        self.assertIsInstance(ba_kw17.id, str)
        self.assertIsInstance(ba_kw17.created_at, datetime.datetime)
        self.assertIsInstance(ba_kw17.updated_at, datetime.datetime)
        self.assertIsInstance(ba_kw17.__class__, type)

    def test_save(self):
        """Test save method"""

        ba = BaseModel()
        temp = ba.__dict__['updated_at']
        self.assertFalse(path.isfile('file.json'))
        ba.save()
        self.assertTrue(path.isfile('file.json'))
        self.assertNotEqual(ba.__dict__['updated_at'], temp)
        temp = ba.__dict__['updated_at']
        models.storage.reload()
        self.assertEqual(ba.__dict__['updated_at'], temp)

    def test_to_dict(self):
        """Test to_dict method"""

        ba = BaseModel()
        ba.age = 28
        ba.size = "tall"
        for k, v in ba.__dict__.items():
            if k != 'updated_at' and k != 'created_at':
                self.assertIn(k, ba.to_dict())
                self.assertEqual(v, ba.to_dict()[k])
        self.assertEqual(ba.to_dict()['__class__'], ba.__class__.__name__)
        self.assertEqual(ba.to_dict()['updated_at'], ba.updated_at.isoformat())
        self.assertEqual(ba.to_dict()['created_at'], ba.created_at.isoformat())
        self.assertEqual(ba.to_dict()['age'], 28)
        self.assertEqual(ba.to_dict()['size'], 'tall')
        self.assertIsInstance(ba.to_dict(), dict)

    def test_str(self):
        """Test __str__ method"""

        bs = BaseModel()
        string = '['+bs.__class__.__name__+']'+' ('+bs.id+') '+str(bs.__dict__)
        self.assertEqual(string, bs.__str__())
