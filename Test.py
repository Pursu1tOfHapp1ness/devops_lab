from unittest import TestCase
import Example


class TestExample(TestCase):
    def test_is_Example(self):
        self.assertFalse(Example.moves('DLLR'))
        self.assertFalse(Example.moves('DLRRLLL'))
        self.assertTrue(Example.moves('DURL'))
        self.assertTrue(Example.moves('DDUU'))
