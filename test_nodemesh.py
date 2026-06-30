# test_nodemesh.py
"""
Tests for NodeMesh module.
"""

import unittest
from nodemesh import NodeMesh

class TestNodeMesh(unittest.TestCase):
    """Test cases for NodeMesh class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = NodeMesh()
        self.assertIsInstance(instance, NodeMesh)
        
    def test_run_method(self):
        """Test the run method."""
        instance = NodeMesh()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
