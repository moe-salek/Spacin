from spacin.spacin import Spacin
from spacin import algorithm

import unittest
from unittest.mock import patch


class TestSpacein(unittest.TestCase):
    """Test Spacin class"""

    def setUp(self):
        self.spacin = Spacin()
        self.algorithms = algorithm

    def test_run_algorithm(self):
        """Test algorithm run"""
        algo = self.algorithms.BasicAlgorithm()
        results = [
            algo.run("hellofriend!"),
            algo.run("!@#$hell23456ofriend$%^7890!"),
            algo.run("h e l l o f r i e n  d ! \t \n \t @!@!"),
            algo.run("12414342352hellofriend!1214141"),
            algo.run("HELLOFRIEND!"),
            algo.run("Hello, Friend !"),
        ]

        for res in results:
            self.assertListEqual(["hello", "friend"], res)

    @patch('spacin.algorithm.BaseAlgorithm')
    @patch('spacin.algorithm.BaseAlgorithm')
    def test_run_all_algorithms(self, algo_1, algo_2):
        """Test input string with all algorithms"""
        algo_1.__class__.__name__ = 'algo_1'
        algo_1.run.return_value = ['hello', 'world']
        algo_2.__class__.__name__ = 'algo_2'
        algo_2.run.return_value = ['hello', 'friend']

        algorithms = [algo_1, algo_2]
        results = self.spacin.run_all_algorithms(algorithms, "just a string")

        self.assertDictEqual(
            results,
            {
                'algo_1': ['hello', 'world'],
                'algo_2': ['hello', 'friend']
            }
        )
