from spacin.spacin import Spacin
from spacin.algorithm import BasicAlgorithm

import unittest


class TestSpacein(unittest.TestCase):
    """Test Spacin class"""

    def setUp(self):
        self.spacin = Spacin()
        self.algorithm = BasicAlgorithm()

    def test_run_algorithm(self):
        """Test algorithm run"""
        func = self.algorithm.run
        results = [
            func('hellofriend!'),
            func('!@#$hell23456ofriend$%^7890!'),
            func('h e l l o f r i e n  d ! \t \n \t @!@!'),
            func('12414342352hellofriend!1214141'),
            func('HELLOFRIEND!'),
            func('Hello, Friend !'),
        ]

        for res in results:
            self.assertEqual(res, 'hello friend')
