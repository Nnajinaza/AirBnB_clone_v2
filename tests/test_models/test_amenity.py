#!/usr/bin/python3
""" Tests the 'Amenity' class """
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity


class test_Amenity(test_basemodel):
    """ 'test_Amenity' test class definition """

    def __init__(self, *args, **kwargs):
        """ Initialization of the tests class """
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """ tests the value of the name attribute """
        new = self.value()
        self.assertEqual(type(new.name), str)
