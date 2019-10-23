#!/usr/bin/python3
""" Square test """
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class Square_Test(unittest.TestCase):
    """ Square """
    def test_empty(self):
        """ Empty instantiation """
        with self.assertRaises(TypeError):
            s1 = Square()

    def test_args(self):
        """ Instantiation with 1 more argument """
        with self.assertRaises(TypeError):
            s1 = Square(1, 1, 1, 1, 1)

    def test_ins_is_right(self):
        """ Instantiation """
        s1 = Square(3, 1, 2, 45)
        self.assertEqual(s1.size, 3)
        self.assertEqual(s1.x, 1)
        self.assertEqual(s1.y, 2)
        self.assertEqual(s1.id, 45)

    def test_str_representation(self):
        """ String representation of a square """
        s1 = Square(3, 1, 2, 45)
        self.assertEqual(s1.__str__(), "[Square] (45) 1/2 - 3")

    def test_sizes_setter(self):
        """ Size setter of square class """
        s1 = Square(3, 1, 2, 45)
        s1.size = 27
        self.assertEqual(s1.size, 27)

    def test_update_method(self):
        """ Update method of square """
        s1 = Square(3, 1, 2, 45)
        s1.update(12, 5, 5, 8)
        self.assertEqual(s1.size, 5)
        self.assertEqual(s1.x, 5)
        self.assertEqual(s1.y, 8)
        self.assertEqual(s1.id, 12)
        s1.update(23)
        self.assertEqual(s1.id, 23)
        self.assertEqual(s1.size, 5)
        self.assertEqual(s1.x, 5)
        self.assertEqual(s1.y, 8)
        s1.update(y=4, x=12, size=8, id=6)
        self.assertEqual(s1.size, 8)
        self.assertEqual(s1.x, 12)
        self.assertEqual(s1.y, 4)
        self.assertEqual(s1.id, 6)
        s1.update(x=1)
        self.assertEqual(s1.x, 1)
        s1.update(6, x=23)
        self.assertEqual(s1.id, 6)
        self.assertEqual(s1.x, 1)

    def test_dictionary(self):
        """ Dictionary"""
        s1 = Square(3, 1, 2, 45)
        s1 = Square(3, 1, 2, 45)
        self.assertDictEqual(s1_d, {'x': 1, 'size': 3, 'id': 45, 'y': 2})
