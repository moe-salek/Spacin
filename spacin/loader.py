import os
from os import listdir
from os.path import isfile, join


class Loader:
    """Load data from files into usable data"""

    def __init__(self):
        self.abs_data_dir = os.path.abspath("./data")

    def get_db_wordlists(self):
        """Return dict of wordlist names + abs path in data dir"""
        return {
            file: join(self.abs_data_dir, file)
            for file in listdir(self.abs_data_dir)
            if isfile(join(self.abs_data_dir, file))
        }

    def load_all_wordlists(self):
        """Load all wordlists from data dir and return dict"""
        wordlists_db = self.get_db_wordlists()
        wordlists = {}
        for name in wordlists_db.keys():
            wordlists[name] = self.load_file(wordlists_db[name])
        return wordlists

    @staticmethod
    def load_file(filepath):
        """Load data from file"""
        with open(filepath, 'r') as file:
            return file.read().splitlines()
