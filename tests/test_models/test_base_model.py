#!/usr/bin/python3
""" Tests 'BaseModel' class """
from models.base_model import BaseModel
import unittest
import datetime
from uuid import UUID
import json
import os


class test_basemodel(unittest.TestCase):
    """ 'test_basemodel' test class definition """

    def __init__(self, *args, **kwargs):
        """ Initialization of test class """
        super().__init__(*args, **kwargs)
        self.name = 'BaseModel'
        self.value = BaseModel

    def setUp(self):
        """ Setting objects for use in testing """
        pass

    def tearDown(self):
        """ Frees up all resources used in testing """
        try:
            os.remove('file.json')
        except Exception:
            pass

    def test_default(self):
        """ Tests 'HBNBCommand.default' method """
        i = self.value()
        self.assertEqual(type(i), self.value)

    def test_kwargs(self):
        """ Tests initialization using 'kwargs' """
        i = self.value()
        copy = i.to_dict()
        new = BaseModel(**copy)
        self.assertFalse(new is i)

    def test_kwargs_int(self):
        """ Tests initialization using 'kwargs' """
        i = self.value()
        copy = i.to_dict()
        copy.update({1: 2})
        with self.assertRaises(TypeError):
            new = BaseModel(**copy)

    def test_save(self):
        """ Tests save """
        i = self.value()
        i.save()
        key = self.name + "." + i.id
        with open('file.json', 'r') as f:
            j = json.load(f)
            self.assertEqual(j[key], i.to_dict())

    def test_str(self):
        """ Tests '__str__' special method """
        i = self.value()
        self.assertEqual(str(i), '[{}] ({}) {}'.format(self.name, i.id,
                         i.__dict__))

    def test_todict(self):
        """ Tests 'to_dict()' method """
        i = self.value()
        n = i.to_dict()
        self.assertEqual(i.to_dict(), n)

    def test_kwargs_none(self):
        """ Tests initialization using 'kwargs' """
        n = {None: None}
        with self.assertRaises(TypeError):
            new = self.value(**n)

    def test_kwargs_one(self):
        """ Tests initialization using 'kwargs' """
        n = {'Name': 'test'}
        with self.assertRaises(KeyError):
            new = self.value(**n)

    def test_id(self):
        """ Tests 'id' attribute """
        new = self.value()
        self.assertEqual(type(new.id), str)

    def test_created_at(self):
        """ Tests 'created_at' attribute """
        new = self.value()
        self.assertEqual(type(new.created_at), datetime.datetime)

    def test_updated_at(self):
        """ Tests 'updated_at' attribute """
        new = self.value()
        self.assertEqual(type(new.updated_at), datetime.datetime)
        n = new.to_dict()
        new = BaseModel(**n)
        self.assertFalse(new.created_at == new.updated_at)
