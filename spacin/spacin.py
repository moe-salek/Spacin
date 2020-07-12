from .loader import Loader
from .validator import Validator

class Spacin:
    """Put the damn space(s) between words!"""

    def __init__(self):
        self.loader = Loader()
        self.validator = Validator()

    def basic_algorithm(self, input_str):
        """The simple brute-force algorithm"""
        self.validator.check_input_validation(input_str)
