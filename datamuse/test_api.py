import unittest
import datamuse
from datamuse import Datamuse

class DatamuseTestCase(unittest.TestCase):
    def setUp(self):
        self.api = Datamuse()
        self.max = 5

    # words endpoint
    def test_sounds_like(self):
        args = {'sl': 'orange', 'max': self.max}
        data = self.api.words(**args)
        self.assertTrue(type(data), list)
        print("sounds like", data)

    def test_rhymes(self):
        args = {'rel_rhy': 'orange', 'max': self.max}
        data = self.api.words(**args)
        self.assertTrue(len(data) <= self.max)
        print("rhyme", data)

    def test_near_rhymes(self):
        args = {'rel_nry': 'orange', 'max': self.max}
        data = self.api.words(**args)
        self.assertTrue(len(data) <= self.max)
        print("near rhyme", data)

    def test_bad_request(self):
        args = {'foo':42}
        with self.assertRaises(ValueError):
            data = self.api.words(**args)

# though really you can just run `nosetests -sv` from this directory
if __name__ == "__main__":
    unittest.main()