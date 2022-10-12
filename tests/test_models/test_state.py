#!/usr/bin/python3
""" Tests 'State' class """
from tests.test_models.test_base_model import test_basemodel
from models.state import State


class test_state(test_basemodel):
    """ 'test_state' test class definition """

    def __init__(self, *args, **kwargs):
        """ Initialization of class """
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """ Tests 'name' attribute """
        new = self.value()
        self.assertEqual(type(new.name), str)
