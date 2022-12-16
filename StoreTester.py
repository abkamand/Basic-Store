# Author: Andrew Kamand
# Date: 1/15/2020
# Description: Unit tests for Store.py (our online store simulator) that test various functions to make sure they work.

import unittest
from Store import Product, Customer, Store, InvalidCheckoutError


class TestStore(unittest.TestCase):
    """Contains unit tests for various Store.py functions."""
    def test_1(self):
        """Tests get_id_code function in Product class (assertEqual)"""
        # create a product object
        p1 = Product("5", "iPhone", "cellular phone made by apple", 500, 5)

        self.assertEqual(p1.get_id_code(), "5")

    def test_2(self):
        """Tests get_title function in Product class (assertAlmostEqual)."""
        # create a product object
        p1 = Product("5", "iPhone", "cellular phone made by apple", 500, 5)

        self.assertAlmostEqual(p1.get_title(), "iPhone")

    def test_3(self):
        """Tests get_price function in Product class (assertNotEqual)."""
        # create a product object
        p1 = Product("5", "iPhone", "cellular phone made by apple", 500, 5)

        self.assertNotEqual(p1.get_price(), 400)

    def test_4(self):
        """Tests is_premium_member function in Customer class (assertTrue)."""
        # create a customer object
        c1 = Customer("Cindy", "XYZ", True)

        self.assertTrue(c1.is_premium_member(), True)

    def test_5(self):
        """Tests get_name function in Customer class (assertEqual)."""
        # create a customer object
        c1 = Customer("Cindy", "XYZ", True)

        self.assertEqual(c1.get_name(), "Cindy")





