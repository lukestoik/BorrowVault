# test_borrowvault.py
"""
Tests for BorrowVault module.
"""

import unittest
from borrowvault import BorrowVault

class TestBorrowVault(unittest.TestCase):
    """Test cases for BorrowVault class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = BorrowVault()
        self.assertIsInstance(instance, BorrowVault)
        
    def test_run_method(self):
        """Test the run method."""
        instance = BorrowVault()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
