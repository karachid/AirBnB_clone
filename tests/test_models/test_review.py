#!/usr/bin/python3
"""
Unittest for the Review class
Test files by using the following command line:
python3 -m unittest tests/test_models/test_review.py
"""
import unittest
import pep8
from os import path, remove
import datetime
import models
from models import review
from models.review import Review
from models.engine.file_storage import FileStorage


class TestReview(unittest.TestCase):
    """ Declares TestReview Class """

    def setUp(self):
        """
        Assigns "" to the public class attributes of the Review class
        Method called to prepare the test fixture. It gets called immediately
        before calling the test method; other than AssertionError or SkipTest
        """
        Review.place_id = ""
        Review.user_id = ""
        Review.text = ""
        FileStorage._FileStorage__objects = {}
        FileStorage._FileStorage__file_path = "file.json"

    def tearDown(self):
        """
        Deletes the public class attributes of the Review class
        Method called immediately after the test method has been called and
        the result recorded
        """
        del Review.place_id
        del Review.user_id
        del Review.text
        del FileStorage._FileStorage__file_path
        del FileStorage._FileStorage__objects
        if path.exists("file.json"):
            remove("file.json")

    def test_pep8_conformance(self):
        """ Tests that Review conforms to PEP8 standards """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/review.py'])
        self.assertEqual(result.total_errors, 0, "Errors (and warnings).")

    def test_class_method_presence(self):
        """ Tests that the Review methods are all defined """
        l1 = dir(Review)
        self.assertIn('__init__', l1)
        self.assertIn('save', l1)
        self.assertIn('to_dict', l1)
        self.assertIn('__str__', l1)

    def test_class_attribute_presence(self):
        """ Tests that the Review attributes are all defined """
        l1 = dir(Review)
        self.assertIn('place_id', l1)
        self.assertIn('user_id', l1)
        self.assertIn('text', l1)

    def test_instance_method_presence(self):
        """ Tests that the Review instance has the same methods """
        l1 = dir(Review())
        self.assertIn('__init__', l1)
        self.assertIn('save', l1)
        self.assertIn('to_dict', l1)
        self.assertIn('__str__', l1)

    def test_instance_attribute_presence(self):
        """ Tests that the Review instance attributes are declared """
        l1 = dir(Review())
        self.assertIn('id', l1)
        self.assertIn('updated_at', l1)
        self.assertIn('created_at', l1)
        self.assertIn('__class__', l1)
        self.assertIn('place_id', l1)
        self.assertIn('user_id', l1)
        self.assertIn('text', l1)

    def test_docstring_presence(self):
        """ Test that  docstring is in Module, Class, and methods """
        self.assertIsNot(review.__doc__, None)
        self.assertIsNot(Review.__doc__, None)
        self.assertIsNot(Review.__init__.__doc__, None)
        self.assertIsNot(Review.save.__doc__, None)
        self.assertIsNot(Review.to_dict.__doc__, None)
        self.assertIsNot(Review.__str__.__doc__, None)

    def test_instantiation(self):
        """ Tests correct instantiation of object Review """

        re = Review()
        self.assertIsInstance(re, Review)
        self.assertIsInstance(re.id, str)
        self.assertIsInstance(re.created_at, datetime.datetime)
        self.assertIsInstance(re.updated_at, datetime.datetime)
        self.assertIsInstance(re.__class__, type)

        re.text = "Good!"
        l1 = dir(re)
        self.assertIn('text', l1)
        self.assertEqual(re.__dict__['text'], 'Good!')

        re_kw1 = Review(**{})
        self.assertIsInstance(re_kw1, Review)
        self.assertIsInstance(re_kw1.id, str)
        self.assertIsInstance(re_kw1.created_at, datetime.datetime)
        self.assertIsInstance(re_kw1.updated_at, datetime.datetime)
        self.assertIsInstance(re_kw1.__class__, type)

    def test_save(self):
        """ Tests save method """

        re = Review()
        temp = re.__dict__['updated_at']
        self.assertFalse(path.isfile('file.json'))
        re.save()
        self.assertTrue(path.isfile('file.json'))
        self.assertNotEqual(re.__dict__['updated_at'], temp)
        temp = re.__dict__['updated_at']
        models.storage.reload()
        self.assertEqual(re.__dict__['updated_at'], temp)

    def test_to_dict(self):
        """ Tests to_dict method """

        re = Review()
        re.text = "Good stay"
        for k, v in re.__dict__.items():
            if k != 'updated_at' and k != 'created_at':
                self.assertIn(k, re.to_dict())
                self.assertEqual(v, re.to_dict()[k])
        self.assertEqual(re.to_dict()['__class__'], re.__class__.__name__)
        self.assertEqual(re.to_dict()['updated_at'], re.updated_at.isoformat())
        self.assertEqual(re.to_dict()['created_at'], re.created_at.isoformat())
        self.assertEqual(re.to_dict()['text'], 'Good stay')
        self.assertIsInstance(re.to_dict(), dict)

    def test_str(self):
        """ Tests __str__ method"""

        re = Review()
        string = '['+re.__class__.__name__+']'+' ('+re.id+') '+str(re.__dict__)
        self.assertEqual(string, re.__str__())
