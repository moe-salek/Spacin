from spacin.validator import Validator

import unittest


class TestValidator(unittest.TestCase):
    """Test Validator class"""

    def setUp(self):
        self.validator = Validator()

    def test_input_empty(self):
        """Test empty input"""
        inputs = [None, [], {}, '']

        for input_str in inputs:
            with self.assertRaises(ValueError):
                self.validator.check_input_validation(input_str)

    def test_input_type(self):
        """Test input type"""
        inputs = [
            [123, 12345],
            ["test", "test2"],
            set('another'),
            {'key': 'value'},
            123,
            123.456,
        ]

        for input_str in inputs:
            with self.assertRaises(TypeError):
                self.validator.check_input_validation(input_str)

    def test_input_is_not_ascii(self):
        """Test input is not ascii"""
        inputs = [
            chr(0),
            chr(96),
            chr(123),
            chr(1000),
        ]

        for input_str in inputs:
            with self.assertRaises(ValueError):
                self.validator.check_input_validation(input_str)

    def test_input_is_ascii(self):
        """Test input is ascii"""
        inputs = [
            chr(97),
            chr(100),
            chr(122)
        ]

        try:
            for ch in inputs:
                self.validator.check_input_validation(ch)
        except Exception:
            self.fail("Raised exception unexpectedly")

    def test_clear_input_no_whitespace(self):
        """Test clears all whitespaces"""
        input_str = '\t \n te st   '

        output = self.validator.clear_input(input_str)
        self.assertEqual(output, 'test')

    def test_clear_input_no_invalid_chars(self):
        """Test clears all invalid characters"""
        input_str = '!@\t#$heLlO,./f(  r)iE_-nd:)  '

        output = self.validator.clear_input(input_str)
        self.assertEqual(output, 'hellofriend')
