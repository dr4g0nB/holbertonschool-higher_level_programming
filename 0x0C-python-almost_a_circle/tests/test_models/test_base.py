#!/usr/bin/python3
""" Base class """
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class Base_Test(unittest.TestCase):
    """ Base_Test """

    def test___init__(self):
        """ __init__ """
        self.assertGreater(__nb_objects, 0)
        self.assertNotIsInstance(nb_objects, __init__, msg=None)

    def test_creation(self):
        """ Creation """
        b = Base()
        test = str(b)
        b1 = Base(12)
        test1 = str(b1)
        b2 = Base()
        test2 = str(b2)
        self.assertTrue(test[:29], '<models.base.Base object at ')
        self.assertTrue(b.id, 1)
        self.assertTrue(test1[:29], '<models.base.Base object at ')
        self.assertTrue(b1.id, 12)
        self.assertTrue(test2[:29], '<models.base.Base object at ')
        self.assertTrue(b2.id, 2)

    def test_nbobjs(self):
        """ id - Increment of nb_objects """
        b = Base()
        test = b.id
        b1 = Base()
        b2 = Base(id=33)
        b3 = Base(-2)
        self.assertTrue(test + 1, b1)
        self.assertTrue(b2.id, 33)
        self.assertTrue(b3.id, -2)

    def test_nb_obj(self):
        """  """
        b = Base(3)
        with self.assertRaises(AttributeError):
            print(b.nb_objects)
        with self.assertRaises(AttributeError):
            print(b.__nb_objects)

    def test_to_json_string(self):
        """ _to_json_string """
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertTrue(type(Base.to_json_string(None)) is str)
        self.assertEqual(Base.to_json_string([]), "[]")
        self.assertTrue(type(Base.to_json_string([])) is str)
        d = {'id': 7, 'width': 10, 'height': 7, 'x': 4, 'y': 8}
        d1 = {'id': 8, 'width': 2, 'height': 5, 'x': 9, 'y': 3}
        convert = Base.to_json_string([d, d1])
        self.assertTrue(type(convert) is str)
        dic = json.loads(convert)
        self.assertEqual(dic, [d, d1])

    def test_jfile_none(self):
        """ Testing with None as a list of instances """
        Rectangle.save_to_file(None)
        with open("Rectangle.json", mode='r') as nfile:
            self.assertEqual([], json.load(nfile))
            Square.save_to_file(None)
        with open("Square.json", mode='r') as nfile:
            self.assertEqual([], json.load(nfile))

    def test_json_string_empty_str(self):
        """ string conversion managing empty strings """
        self.assertEqual(Base.from_json_string(""), [])
        self.assertEqual(Base.from_json_string(None), [])

    def test_from_json_string(self):
        """ from_json_string """
        string = '[{"id": 7, "width": 10, "height": 7, "x": 4, "y": 8}, \
                    {"id": 8, "width": 2, "height": 5, "x": 9, "y": 3}]'
        jsconv = Base.from_json_string(string)
        self.assertTrue(type(jsconv) is list)
        self.assertEqual(len(jsconv), 2)

    def test_jfile_empty(self):
        """ empty list of instances """
        Rectangle.save_to_file([])
        with open("Rectangle.json", mode='r') as nfile:
            self.assertEqual([], json.load(nfile))
            Square.save_to_file([])
        with open("Square.json", mode='r') as nfile:
            self.assertEqual([], json.load(nfile))

    def test_rectangle_creation(self):
        """ creation of a rectangle """
        r = Rectangle(5, 6, 7)
        r_dictionary = r.to_dictionary()
        r1 = Rectangle.create(**r_dictionary)
        self.assertNotEqual(r, r1)

    def test_square_creation(self):
        """ creation of a square """
        s = Square(2, 3, 3, 4)
        s_dictionary = s.to_dictionary()
        s1 = Square.create(**s_dictionary)
        self.assertNotEqual(s, s1)

    def test_rectangle_file(self):
        """ file loads from rectangle """
        r = Rectangle(5, 6, 7)
        r1 = Rectangle(10, 5)
        listrectangles = [r, r1]
        Rectangle.save_to_file(listrectangles)
        listrectangle = Rectangle.load_from_file()
        self.assertNotEqual(listrectangles, listrectangle)

    def test_square_file(self):
        """ file loads from square """
        s = Square(5, 6, 7)
        s1 = Square(10, 5, 6)
        listsquares = [s, s1]
        Square.save_to_file(listsquares)
        listsquare = Square.load_from_file()
        self.assertNotEqual(listsquares, listsquare)

    def test_documentation(self):
        """ Documentation """
        self.assertIsNotNone(Base.__doc__)
        self.assertIsNotNone(Base.__init__.doc)
        self.assertIsNotNone(Base.to_json_string.__doc__)
        self.assertIsNotNone(Base.save_to_file.__doc__)
        self.assertIsNotNone(Base.from_json_string.__doc__)
        self.assertIsNotNone(Base.create.__doc__)

    def test_docs(self):
        """ Doctsring """
        self.assertIsNotNone(Base.__doc__)
