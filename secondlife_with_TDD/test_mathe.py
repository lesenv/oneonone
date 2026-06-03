import unittest as ut
import mathe
import random
from typing import Protocol
from  mock import patch

random.seed(1)

class Aufgabe(Protocol):
    def test_symbol(self):
        ...
    def test_result(self):
        ...

class TestMultiplizieren(ut.TestCase, Aufgabe):

    def setUp(self):
        self.tst = mathe.Multiplizieren()
        self.newAufgabe = self.tst.make_Aufgabe()
        return super().setUp()

    def test_symbol(self):
        self.assertEqual(self.tst.symbol, "x")

    def test_make_Aufgabe(self):
        self.assertEqual(self.newAufgabe, [1, "x", 7] )

    def test_get_result(self):
        '''6x3 = 18'''
        self.assertEqual(self.tst.get_result(), 18)


class TestMathFunction(ut.TestCase):

    def test_get_2_ints_positive(self):
        a, b = mathe.get_2_ints(0, 6)
        self.assertEqual((a, b), (6, 0))
        a, b = mathe.get_2_ints(3, 100072)
        self.assertEqual((a, b), (33435, 15458))

    def test_get_2_ints_negatives(self):
        a, b = mathe.get_2_ints(-4, 5)
        self.assertEqual((a, b), (-2, 5))
        a, b = mathe.get_2_ints(-30, 0)
        self.assertEqual((a, b), (-3, -5))

    def test_get_2_ints_wrong_order(self):
        a, b = mathe.get_2_ints(6, 1)
        self.assertEqual((a, b), (4, 6))

    def test_get_2_ints_same_number(self):
        a, b = mathe.get_2_ints(4,4)
        self.assertEqual((a, b), (4, 4))

        # with self.assertRaises(ValueError) as ve:
        #     a, b = mathe.get_2_ints(3, -4)
        # self.assertTrue("empty range" in str(ve.exception))

 #   def test_get_2_ints_false_not_working_inputs(self):
 #       with self.assertRaises(TypeError) as cm:
##            mathe.get_2_ints(3, "nuiiad")
  #      self.assertEqual('b has to be a number', str(cm.exception))

class TestViewerTerminal(ut.TestCase):
    
    def setUp(self):
        self.viewer = mathe.Terminal()

    def test_output_print_header(self):
        out = self.viewer.header()
        check = ["1x1-Übungen    -  Schluss mit 'zzz', 'ppp' ist neuer Spieler",
                 "================"
                ]
        self.assertEqual(out, check)

    ## testing the conversion from string to int
    @patch("builtins.input", lambda _: "10")
    def test_get_input(self):
        out = self.viewer.get_input("gsuiij")
        self.assertEqual(out, 10)

    def test_get_Aufgabe(self):
        out = self.viewer.get_Aufgabe([45,"*",67])
        self.assertEqual(out, "45 * 67 = ")

if __name__ == "__main__":
    ut.main()