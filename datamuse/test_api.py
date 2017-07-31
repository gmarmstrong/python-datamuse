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

    def test_set_max(self):
        self.assertTrue(self.api.max, 100)
        self.api.set_max_default(10)
        self.assertEquals(self.api.max, 10)
        data = self.api.words(ml='ringing in the ears')
        self.assertEquals(len(data), 10)

    def test_set_max_error(self):
        with self.assertRaises(ValueError):
            self.api.set_max_default(-2)
            self.api.set_max_default(0)
            self.api.set_max_default(1001)


if __name__ == "__main__":
    unittest.main()
