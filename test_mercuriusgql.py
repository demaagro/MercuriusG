# test_mercuriusgql.py
"""
Tests for MercuriusGQL module.
"""

import unittest
from mercuriusgql import MercuriusGQL

class TestMercuriusGQL(unittest.TestCase):
    """Test cases for MercuriusGQL class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = MercuriusGQL()
        self.assertIsInstance(instance, MercuriusGQL)
        
    def test_run_method(self):
        """Test the run method."""
        instance = MercuriusGQL()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
