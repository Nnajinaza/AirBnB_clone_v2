#!/usr/bin/python3
""" Tests 'Review' class """
from tests.test_models.test_base_model import test_basemodel
from models.review import Review


class test_review(test_basemodel):
    """ 'test_review' test class definition """

    def __init__(self, *args, **kwargs):
        """ Initialization of class """
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
        """ Tests 'place_id' attribute """
        new = self.value()
        self.assertEqual(type(new.place_id), str)

    def test_user_id(self):
        """ Tests 'user_id' attribute """
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_text(self):
        """ Tests 'text' attribute """
        new = self.value()
        self.assertEqual(type(new.text), str)
