class Loader:
    """Load data from files into usable data"""

    @staticmethod
    def load_file(filepath):
        """Load data from file"""
        with open(filepath, 'r') as f:
            return f.read().splitlines()
