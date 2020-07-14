import unittest

from spacin.algorithm import BaseAlgorithm, BasicAlgorithm


class TestBaseAlgorithm(unittest.TestCase):
    """Test the Base Algorithm abstract class"""

    def test_str(self):
        """Test __str__ function"""
        algorithm = BaseAlgorithm()

        self.assertEqual('BaseAlgorithm', algorithm.__str__())


class TestBasicAlgorithm(unittest.TestCase):
    """Test functionality of Basic Algorithm"""

    def setUp(self):
        self.algorithm = BasicAlgorithm()
        self.wordlists = self.algorithm.wordlists

    def test_string_breaker_not_empty(self):
        """Test string_breaker returns non-empty set"""
        input_str = "test"
        result = self.algorithm.string_breaker(input_str)

        self.assertIsNotNone(result)
        self.assertTrue(result)
        self.assertIsInstance(result, set)

    def test_string_breaker_return(self):
        """Test string_breaker return correct set"""
        input_str = "helloworld"
        result = self.algorithm.string_breaker(input_str)

        self.assertIn("he", result)
        self.assertIn("hello", result)
        self.assertIn("world", result)

    def test_get_components(self):
        """Test to get correct components of a string"""
        text = "hello"
        components = self.algorithm.get_components(text)

        expected = ["hello", "lo", "ll", "he", "hell", "el"]
        self.assertCountEqual(components, expected)

    def test_filter_result_list_length(self):
        """Test to filter the best result by the shortest list"""
        results = [
            ["hello", "friends"],
            ["hell", "o", "friend", "s"],
            ["he", "l", "lo", "fri", "end", "s"],
        ]
        final_res = self.algorithm.filter_result(results)

        self.assertListEqual(final_res, ["hello", "friends"])

    def test_filter_result_longest_word(self):
        """Test to filter the best result by the longest words"""
        results = [
            ["thisis", "justatest"],
            ["thisisjusta", "test"],
        ]
        final_res = self.algorithm.filter_result(results)

        self.assertListEqual(final_res, ["thisisjusta", "test"])

    def test_deep_with_startswith(self):
        """Test to find correct ways of creating string with its components"""
        text = self.algorithm.validator.clear_input("hell")
        components = self.algorithm.string_breaker(text)
        results = self.algorithm.deep_with_startswith(
            [text, 0, components],
            [],
            []
        )
        expected = [
            ['he', 'l', 'l'],
            ['he', 'll'],
            ['hell'],
            ['h', 'el', 'l'],
            ['h', 'e', 'l', 'l'],
            ['h', 'e', 'll']
        ]

        self.assertCountEqual(results, expected)
