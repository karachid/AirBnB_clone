#!/usr/bin/python3
"""
Unittest for the City class
Test files by using the following command line:
python3 -m unittest tests/test_models/test_city.py
"""
import unittest
import pep8
from os import path, remove
import datetime
import models
from models import city
from models.city import City
from models.engine.file_storage import FileStorage


class TestCity(unittest.TestCase):
    """define variables and methods"""

    def setUp(self):
        """
        Assieng "" to  the public class attributes of the City
        Method called to prepare the test fixture. it gets called immediately
        before calling the test method; other than AssertionError or SkipTest
        """
        City.state_id = ""
        City.name = ""
        FileStorage._FileStorage__objects = {}
        FileStorage._FileStorage__file_path = "file.json"

    def tearDown(self):
        """
        Deletes the public class attributes of the City class
        Method called immediately after the test method has been called and
        the result recorded
        """
        del City.state_id
        del City.name
        del FileStorage._FileStorage__file_path
        del FileStorage._FileStorage__objects
        if path.exists("file.json"):
            remove("file.json")

    def test_pep8_conformance(self):
        """ Tests that City conforms to PEP8 standards """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/city.py'])
        self.assertEqual(result.total_errors, 0, "Errors (and warnings).")

    def test_class_method_presence(self):
        """ Tests that the City methods are all defined """
        l1 = dir(City)
        self.assertIn('__init__', l1)
        self.assertIn('save', l1)
        self.assertIn('to_dict', l1)
        self.assertIn('__str__', l1)

    def test_class_attribute_presence(self):
        """ Test that the City attributes are all declared """
        l1 = dir(City)
        self.assertIn('state_id', l1)
        self.assertIn('name', l1)

    def test_instance_method_presence(self):
        """ Tests that the City instance has the same methods"""
        l1 = dir(City())
        self.assertIn('__init__', l1)
        self.assertIn('save', l1)
        self.assertIn('to_dict', l1)
        self.assertIn('__str__', l1)

    def test_instance_attribute_presence(self):
        """ Tests that the City instance attributes are defined"""
        l1 = dir(City())
        self.assertIn('id', l1)
        self.assertIn('updated_at', l1)
        self.assertIn('created_at', l1)
        self.assertIn('__class__', l1)
        self.assertIn('state_id', l1)
        self.assertIn('name', l1)

    def test_docstring_presence(self):
        """ Tests that docstring is in Module, Class, and methods """
        self.assertIsNot(city.__doc__, None)
        self.assertIsNot(City.__doc__, None)
        self.assertIsNot(City.__init__.__doc__, None)
        self.assertIsNot(City.save.__doc__, None)
        self.assertIsNot(City.to_dict.__doc__, None)
        self.assertIsNot(City.__str__.__doc__, None)

    def test_instantiation(self):
        """ Tests correct instantiation of object City"""

        ci = City()
        self.assertIsInstance(ci, City)
        self.assertIsInstance(ci.id, str)
        self.assertIsInstance(ci.created_at, datetime.datetime)
        self.assertIsInstance(ci.updated_at, datetime.datetime)
        self.assertIsInstance(ci.__class__, type)

        ci.name = "Rabat"
        l1 = dir(ci)
        self.assertIn('name', l1)
        self.assertEqual(ci.__dict__['name'], 'Rabat')

        ci_kw1 = City(**{})
        self.assertIsInstance(ci_kw1, City)
        self.assertIsInstance(ci_kw1.id, str)
        self.assertIsInstance(ci_kw1.created_at, datetime.datetime)
        self.assertIsInstance(ci_kw1.updated_at, datetime.datetime)
        self.assertIsInstance(ci_kw1.__class__, type)

    def test_save(self):
        """ Tests save method"""

        ci = City()
        temp = ci.__dict__['updated_at']
        self.assertFalse(path.isfile('file.json'))
        ci.save()
        self.assertTrue(path.isfile('file.json'))
        self.assertNotEqual(ci.__dict__['updated_at'], temp)
        temp = ci.__dict__['updated_at']
        models.storage.reload()
        self.assertEqual(ci.__dict__['updated_at'], temp)

    def test_to_dict(self):
        """ Tests to_dict method"""

        ci = City()
        ci.name = "Rabat"
        for k, v in ci.__dict__.items():
            if k != 'updated_at' and k != 'created_at':
                self.assertIn(k, ci.to_dict())
                self.assertEqual(v, ci.to_dict()[k])
        self.assertEqual(ci.to_dict()['__class__'], ci.__class__.__name__)
        self.assertEqual(ci.to_dict()['updated_at'], ci.updated_at.isoformat())
        self.assertEqual(ci.to_dict()['created_at'], ci.created_at.isoformat())
        self.assertEqual(ci.to_dict()['name'], 'Rabat')
        self.assertIsInstance(ci.to_dict(), dict)

    def test_str(self):
        """ Tests __str__ method """

        ci = City()
        string = '['+ci.__class__.__name__+']'+' ('+ci.id+') '+str(ci.__dict__)
        self.assertEqual(string, ci.__str__())
