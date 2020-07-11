from spacin.loader import Loader

import unittest
from os import listdir


class TestLoader(unittest.TestCase):
    """Test Loader class"""

    def setUp(self):
        self.data_dir = "./data"

    def test_files_exist_in_data_dir(self):
        """Test data dir is not empty"""
        loader = Loader()
        wordlist_dict = loader.get_db_wordlists()

        self.assertTrue(listdir(self.data_dir))
        self.assertIsNotNone(wordlist_dict)
        self.assertEqual(type(wordlist_dict), dict)

    def test_load_file_file_not_exists(self):
        """Test given filepath exists"""
        filapath = "NOT a file path"

        with self.assertRaises(FileNotFoundError):
            Loader().load_file(filapath)

        filapath = "NOT a file path"
