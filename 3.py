import unittest
import re
from hamcrest import *
from assertpy import *


class displaySong():
    def display(self, *args):
        song = '''
On the first day of Christmas my true love gave to me: a Partridge in a Pear Tree.

On the second day of Christmas my true love gave to me: two Turtle Doves, and a Partridge in a Pear Tree.

On the third day of Christmas my true love gave to me: three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.

On the fourth day of Christmas my true love gave to me: four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.

On the fifth day of Christmas my true love gave to me: five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.

On the sixth day of Christmas my true love gave to me: six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.

On the seventh day of Christmas my true love gave to me: seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.

On the eighth day of Christmas my true love gave to me: eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.

On the ninth day of Christmas my true love gave to me: nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.

On the tenth day of Christmas my true love gave to me: ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.

On the eleventh day of Christmas my true love gave to me: eleven Pipers Piping, ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.

On the twelfth day of Christmas my true love gave to me: twelve Drummers Drumming, eleven Pipers Piping, ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.'''
        splitted = re.split("\n", song)
        final = [k for k in splitted if k != '']
        if len(args) not in [1, 2]:
            raise ValueError("You can insert only 1 or 2 integers")
        if args[0] > len(final):
            raise ValueError("Index of starting line cannot be bigger than number of all lines")
        for value in args:
            if type(value) is not int or value < 0:
                raise ValueError("You can insert only 2 positive integers")
        if len(args) == 2:
             print("\n".join(final[args[0]:args[1]]))
        elif len(args) == 1:
            print("\n".join(final[args[0]]))


class Tests(unittest.TestCase):
    def setUp(self):
        self.temp = displaySong()

    def test_raise_Exception_0_values(self):
        assert_warn(self.temp.display)

    def test_raise_Exception_more_than_2_values(self):
        assert_warn(self.temp.display, 3, 6, 9)

    def test_raise_Exception_incorrect_data_type_str(self):
        assert_warn(self.temp.display, "3")

    def test_raise_Exception_incorrect_data_type_negative(self):
        assert_warn(self.temp.display, 3, -7)

    def test_raise_Exception_incorrect_data_type_starting_index_too_big(self):
        assert_warn(self.temp.display, 100)

    def test_raise_Exception_incorrect_data_type_list(self):
        assert_warn(self.temp.display, [1, 8])

    def test_raise_Exception_incorrect_data_type_tuple(self):
        assert_warn(self.temp.display, (3, 6))

    def test_raise_Exception_incorrect_data_type_dict(self):
        assert_warn(self.temp.display, {"one": 1, "four": 4})

    def test_raise_Exception_incorrect_data_type_float(self):
        assert_warn(self.temp.display, 3.6)

    def test_is_positive_first_line(self):
        assert_that(self.temp.display(0), "On the first day of Christmas my true love gave to me: a Partridge in a Pear Tree.")

    def test_is_positive_last_line(self):
        self.assertEqual(self.temp.display(11), "On the twelfth day of Christmas my true love gave to me: twelve Drummers Drumming, eleven Pipers Piping, ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.")


    def test_is_positive_range(self):
        self.assertEqual(self.temp.display(9, 11), '''On the tenth day of Christmas my true love gave to me: ten 
        Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, 
        five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree. On 
        the eleventh day of Christmas my true love gave to me: eleven Pipers Piping, ten Lords-a-Leaping, nine Ladies 
        Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling 
        Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree. On the twelfth day of Christmas 
        my true love gave to me: twelve Drummers Drumming, eleven Pipers Piping, ten Lords-a-Leaping, nine Ladies 
        Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling 
        Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.''')


tests = Tests()
tests.setUp()
tests.test_raise_Exception_incorrect_data_type_float()
tests.test_raise_Exception_incorrect_data_type_starting_index_too_big()
tests.test_raise_Exception_incorrect_data_type_dict()
tests.test_raise_Exception_incorrect_data_type_negative()
tests.test_raise_Exception_incorrect_data_type_str()
tests.test_raise_Exception_incorrect_data_type_tuple()
tests.test_raise_Exception_0_values()
tests.test_raise_Exception_more_than_2_values()
tests.test_raise_Exception_incorrect_data_type_list()
tests.test_is_positive_range()
tests.test_is_positive_first_line()
tests.test_is_positive_last_line()



