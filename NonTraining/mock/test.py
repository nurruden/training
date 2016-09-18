#-*-coding:utf-8-*-
#/usr/bin/env python
__author__ = "Allan"
import unittest
from function import add_and_multiply
import mock


class MyTestCase(unittest.TestCase):
    @mock.patch('function.multiply')
    def test_add_and_multiply(self,mock_multiply):
        x = 3
        y = 5

        mock_multiply.return_value = 15

        addition, multiple = add_and_multiply(x, y)

        mock_multiply.assert_called_once_with(3, 5)

        self.assertEqual(8, addition)
        self.assertEqual(15, multiple)

if __name__ == "__main__":
    unittest.main()