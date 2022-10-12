#!/usr/bin/python3
""" Tests 'User' class """
from tests.test_models.test_base_model import test_basemodel
from models.user import User


class test_User(test_basemodel):
    """ 'test_User' test class definition """

    def __init__(self, *args, **kwargs):
        """ Initialization of the class """
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_first_name(self):
        """ Tests 'first_name' attribute """
        new = self.value()
        self.assertEqual(type(new.first_name), str)

    def test_last_name(self):
        """ Tests 'last_name' attribute """
        new = self.value()
        self.assertEqual(type(new.last_name), str)

    def test_email(self):
        """ Tests 'email' attribute """
        new = self.value()
        self.assertEqual(type(new.email), str)

    def test_password(self):
        """ Tests 'password' attribute """
        new = self.value()
        self.assertEqual(type(new.password), str)
