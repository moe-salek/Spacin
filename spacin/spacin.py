"""This module is developed to put space correctly between rubbish non-sense
strings so it could be more readable.
example:
"hellofriendthisissohardtoread" -> "hello friend this is so hard to read"
See? It might help some people Some times. Specially Germans. Probably. lol.
"""


class Spacin:
    """Put the damn space(s) between words!"""

    @staticmethod
    def run(algorithm, input_str, clear=True):
        """Run algorithm with given string"""
        result = algorithm.run(input_str, clear)
        return result

    @staticmethod
    def run_all_algorithms(algorithms, input_str, clear=True):
        """Run all algorithms with given string"""
        results = {}
        for algorithm in algorithms:
            result = algorithm.run(input_str, clear)
            results[algorithm.__class__.__name__] = result
        return results
