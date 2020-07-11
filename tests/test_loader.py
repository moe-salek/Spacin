from spacin.loader import Loader

import unittest
from os import listdir
from os.path import isfile, join, abspath


class TestLoader(unittest.TestCase):
    """Test to load data from files into usable data"""

    def setUp(self):
        """Set up class"""
        self.data_dir = "./data"

    def test_files_exist_in_data_dir(self):
        """Test data dir is not empty"""
        self.assertTrue(listdir(self.data_dir))

    def test_load_file_file_not_exists(self):
        """Test given filepath exists"""
        filapath = "NOT a file path"

        with self.assertRaises(FileNotFoundError):
            Loader().load_file(filapath)
