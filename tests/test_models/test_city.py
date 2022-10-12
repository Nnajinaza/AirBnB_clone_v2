#!/usr/bin/python3
""" Tests the City class """
from tests.test_models.test_base_model import test_basemodel
from models.city import City


class test_City(test_basemodel):
    """ 'test_City' test class definition """

    def __init__(self, *args, **kwargs):
        """ Initialize test class """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """ Tests 'state_id' attribute """
        new = self.value()
        self.assertEqual(type(new.state_id), str)

    def test_name(self):
        """ Tests 'name' attribute """
        new = self.value()
        self.assertEqual(type(new.name), str)
