#!/usr/bin/python3
""" Tests class State"""
import unittest
from models.state import State


class TestState(unittest.TestCase):
    """Test State class"""

    def test_attributes(self):
        """Test State attributess"""
        state = State()
        self.assertEqual(state.name, "")

    def test_str_representation(self):
        """Test the __str__ method"""
        state = State()
        str_rep = str(state)
        self.assertIsInstance(str_rep, str)
        self.assertIn("[State]", str_rep)
        self.assertIn("'id':", str_rep)
        self.assertIn("'created_at':", str_rep)
        self.assertIn("'updated_at':", str_rep)


if __name__ == '__main__':
    unittest.main()
