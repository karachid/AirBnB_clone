#!/usr/bin/python3
"""
Unittest for the State class
Test files by using the following command line:
python3 -m unittest tests/test_models/test_state.py
"""
import unittest
import pep8
from os import path, remove
import datetime
import models
from models import state
from models.state import State
from models.engine.file_storage import FileStorage


class TestState(unittest.TestCase):
    """ Declares TestState Class"""

    def setUp(self):
        """
        Assigns an empty string to the public class attributes of the State
        Method called to prepare the test fixture.
        It gets called immediately
        before calling the test method; other than AssertionError or SkipTest
        """
        State.name = ""
        FileStorage._FileStorage__objects = {}
        FileStorage._FileStorage__file_path = "file.json"

    def tearDown(self):
        """
        Deletes the class attributes of the State class back to ""
        Method called immediately after the test method has been called and
        the result recorded
        """
        del State.name
        del FileStorage._FileStorage__file_path
        del FileStorage._FileStorage__objects
        if path.exists("file.json"):
            remove("file.json")

    def test_pep8_conformance(self):
        """Tests that State conforms to PEP8i standard """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/state.py'])
        self.assertEqual(result.total_errors, 0, "Errors (and warnings).")

    def test_class_method_presence(self):
        """Test that the State methods are declared"""
        l1 = dir(State)
        self.assertIn('__init__', l1)
        self.assertIn('save', l1)
        self.assertIn('to_dict', l1)
        self.assertIn('__str__', l1)

    def test_class_attribute_presence(self):
        """Test that the State name attribute is declared """
        l1 = dir(State)
        self.assertIn('name', l1)

    def test_instance_method_presence(self):
        """Test that the State instance has the same methods"""
        l1 = dir(State())
        self.assertIn('__init__', l1)
        self.assertIn('save', l1)
        self.assertIn('to_dict', l1)
        self.assertIn('__str__', l1)

    def test_instance_attribute_presence(self):
        """Tests that the State instance attributes are all there"""
        l1 = dir(State())
        self.assertIn('id', l1)
        self.assertIn('updated_at', l1)
        self.assertIn('created_at', l1)
        self.assertIn('__class__', l1)
        self.assertIn('name', l1)

    def test_docstring_presence(self):
        """Test that Module, Class, and methods all have a docstring"""
        self.assertIsNot(state.__doc__, None)
        self.assertIsNot(State.__doc__, None)
        self.assertIsNot(State.__init__.__doc__, None)
        self.assertIsNot(State.save.__doc__, None)
        self.assertIsNot(State.to_dict.__doc__, None)
        self.assertIsNot(State.__str__.__doc__, None)

    def test_instantiation(self):
        """Test proper instantiation of object 'User()'"""

        st = State()
        self.assertIsInstance(st, State)
        self.assertIsInstance(st.id, str)
        self.assertIsInstance(st.created_at, datetime.datetime)
        self.assertIsInstance(st.updated_at, datetime.datetime)
        self.assertIsInstance(st.__class__, type)

        st.name = "NYC"
        l1 = dir(st)
        self.assertIn('name', l1)
        self.assertEqual(st.__dict__['name'], 'NYC')

        st_kw1 = State(**{})
        self.assertIsInstance(st_kw1, State)
        self.assertIsInstance(st_kw1.id, str)
        self.assertIsInstance(st_kw1.created_at, datetime.datetime)
        self.assertIsInstance(st_kw1.updated_at, datetime.datetime)
        self.assertIsInstance(st_kw1.__class__, type)

    def test_save(self):
        """ Tests save method"""

        stt = State()
        temp = stt.__dict__['updated_at']
        self.assertFalse(path.isfile('file.json'))
        stt.save()
        self.assertTrue(path.isfile('file.json'))
        self.assertNotEqual(stt.__dict__['updated_at'], temp)
        temp = stt.__dict__['updated_at']
        models.storage.reload()
        self.assertEqual(stt.__dict__['updated_at'], temp)

    def test_to_dict(self):
        """ Tests to_dict method """

        stt = State()
        stt.name = "NYC"
        for k, v in stt.__dict__.items():
            if k != 'updated_at' and k != 'created_at':
                self.assertIn(k, stt.to_dict())
                self.assertEqual(v, stt.to_dict()[k])
        self.assertEqual(stt.to_dict()['__class__'], stt.__class__.__name__)
        up = stt.updated_at.isoformat()
        cr = stt.created_at.isoformat()
        self.assertEqual(stt.to_dict()['updated_at'], up)
        self.assertEqual(stt.to_dict()['created_at'], cr)
        self.assertEqual(stt.to_dict()['name'], "NYC")
        self.assertIsInstance(stt.to_dict(), dict)

    def test_str(self):
        """Tests __str__ method"""

        stt = State()
        c = '['+stt.__class__.__name__+']'+' ('+stt.id+') '+str(stt.__dict__)
        self.assertEqual(c, stt.__str__())
