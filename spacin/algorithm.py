import abc

from .loader import Loader
from .validator import Validator


class BaseAlgorithm:
    """Abstract Algorithm template"""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def run(self, input_str, clean=True):
        """Run the algorithm with the given input string"""
        return


class BasicAlgorithm(BaseAlgorithm):
    """The simple brute-force algorithm
    It is considered the input_str is grammatically correct.
    """

    def __init__(self):
        self.loader = Loader()
        self.validator = Validator()
        self.wordlists = self.loader.load_all_wordlists()

    def run(self, input_str, clean=True):
        if clean:
            input_str = self.validator.clear_input(input_str)
        self.validator.check_input_validation(input_str)

        wordlist = self.wordlists['wordlist_popular_20k.txt']
        wordlist.sort(reverse=True)
