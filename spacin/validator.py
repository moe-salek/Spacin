"""The goal of this module is to discover and format bad-input-strings!"""


class Validator:
    """Class to validate input"""

    def __init__(self):
        self.valid_chars = [chr(val) for val in range(97, 122+1)]  # a-z
        self.remove_chars = '.,!?/-+@#$%^&*_="\'\\(){}[]:;' + '0123456789'

    def clear_input(self, input_str):
        """Removes the invalid chars and makes it lowercase"""
        input_str = "".join(input_str.split())  # remove whitespaces
        for inv in self.remove_chars:
            input_str = input_str.replace(inv, '')
        return input_str.lower()

    def check_input_validation(self, input_str):
        """Check input validation"""
        if not input_str:
            raise ValueError("Input string can't be empty(None)")

        if not isinstance(input_str, str):
            raise TypeError(
                "Input must be in string type",
                f"It got {type(input_str)} instead"
            )

        if len(input_str) < 1:
            raise ValueError("Input string must have 1 or more characters")

        for char in input_str:
            if char not in self.valid_chars:
                raise ValueError("Input character invalid (must be a-z)")
