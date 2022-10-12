'''Tests the functionality of the hbnb console.'''

import unittest
from unittest.mock import patch
from console import HBNBCommand
from io import StringIO
from uuid import UUID


class TestConsole(unittest.TestCase):
    '''Tests the functionality of the console '''
    def setUp(self):
        ''' Sets up the test environment '''
        self.string_regex = "[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}"
        self.create_keys = 'create Place city_id="0001" user_id="0001" name="My_little_house" number_rooms=4 number_bathrooms=2 max_guest=10 price_by_night=300 latitude=37.773972 longitude=-122.431297'


    def test_all_help(self):
        ''' Tests the help functionality of the 'all' command'''
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help all")
            self.assertEqual(type(f.getvalue()), str)

    def test_all(self):
        ''' Tests the 'all' command '''
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all BaseModel")
            output = eval(f.getvalue())
            self.assertEqual(type(output), list)

    def test_create_help(self):
        ''' Tests the help functionality of the 'create' '''
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('help create')
            self.assertEqual(type(f.getvalue()), str)

    def test_create_command(self):
        ''' Tests the basic variant of the 'create' command'''
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create BaseModel')
            returnedID = f.getvalue()
            self.assertRegex(returnedID, self.string_regex)

    def test_create_command_with_keywords(self):
        ''' Tests a more advanced variant of the 'create' command'''
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(self.create_keys)
            returnedID = f.getvalue()
            self.assertRegex(returnedID, self.string_regex)


if __name__ == '__main__':
    unittest.main()
