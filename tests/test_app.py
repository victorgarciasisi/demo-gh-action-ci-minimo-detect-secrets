import unittest

from app import add


class TestApp(unittest.TestCase):
    def test_add(self) -> None:
        self.assertEqual(add(2, 3), 5)
