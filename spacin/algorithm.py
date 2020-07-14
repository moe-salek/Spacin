"""This module contains the algorithms to be used to break strings and put
spaces correctly between the words! (lol)
"""

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

    def __str__(self):
        return self.__class__.__name__


class BasicAlgorithm(BaseAlgorithm):
    """The simple brute-force algorithm
    It is assumed that input_str is grammatically correct.
    """

    def __init__(self):
        """Initialize Basic Algorithm"""
        self.loader = Loader()
        self.validator = Validator()
        self.wordlists = self.loader.load_all_wordlists()

    def run(self, input_str, clean=True):
        """Run Basic Algorithm with given parameters"""
        if clean:
            input_str = self.validator.clear_input(input_str)
        self.validator.check_input_validation(input_str)

        components = self.get_components(input_str)
        results = self.deep_with_startswith([input_str, 0, components], [], [])
        final_res = self.filter_result(results)
        return final_res

    def string_breaker(self, input_str):
        """Break input string into a set of the string components"""
        result = set()
        for word in next(iter(self.wordlists.values())):
            if word in input_str:
                result.add(word)
        return result

    def get_components(self, input_str):
        """Get components (customized: excluding certain words/chars) of a
        text"""
        components = self.string_breaker(input_str)
        components = [
            comp
            for comp in components
            if len(comp) != 1 or comp in ("a", "an", "i")
        ]
        return components

    @staticmethod
    def filter_result(results):
        """Filter the best suitable result from all the results"""
        if not results:
            return []
        final_res = min(results, key=len)  # finds the smallest list by len()
        return final_res

    def deep_with_startswith(self, text_stuff, burden, results):
        """Find ways to construct text by given components"""
        text, start_index, components = text_stuff
        entrylist = []
        for constr in components:
            if text.startswith(constr, start_index):
                entrylist.append(constr)

        if not entrylist and start_index == len(text):
            results.append(burden)

        for entry in entrylist:
            idx = start_index + len(entry)
            heavier_burden = burden + [entry]
            self.deep_with_startswith(
                [text, idx, components], heavier_burden, results
            )

        return results
