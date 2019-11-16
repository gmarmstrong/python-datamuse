#!/usr/bin/env python3
import json
import unittest
from urllib.parse import urljoin

import pkg_resources
import responses

from datamuse import Datamuse


class DatamuseTestCase(unittest.TestCase):

    @responses.activate
    def setUp(self):
        self.max = 5
        self.api = Datamuse()
        _api_url = 'https://api.datamuse.com/words'

        _fp = pkg_resources.resource_filename(__name__, 'fixtures/orange.json')
        with open(_fp) as response_json:
            response_json = json.load(response_json)

        responses.add(responses.GET,
                      urljoin(_api_url, '?sl=orange?max=5'),
                      json=response_json, status=200)
        responses.add(responses.GET,
                      urljoin(_api_url, '?rel_rhy=orange?max=5'),
                      json=response_json, status=200)
        responses.add(responses.GET,
                      urljoin(_api_url, '?rel_nry=orange?max=5'),
                      json=response_json, status=200)

        _fp = pkg_resources.resource_filename(__name__, 'fixtures/ringing.json')
        with open(_fp) as response_json:
            response_json = json.load(response_json)

        responses.add(responses.GET,
                      urljoin(_api_url, f'?ml=ringing+in+the+ears'),
                      json=response_json, status=200)


        _fp = pkg_resources.resource_filename(__name__, 'fixtures/por.json')
        with open(_fp) as response_json:
            response_json = json.load(response_json)
        responses.add(responses.GET,
                      urljoin(_api_url, f'?s=por&max=3'),
                      json=response_json, status=200)


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

    def test_set_max(self):
        self.assertTrue(self.api.max, 100)
        self.api.set_max_default(10)
        self.assertEqual(self.api.max, 10)
        data = self.api.words(ml='ringing in the ears')
        self.assertEqual(len(data), 10)

    def test_set_max_error(self):
        with self.assertRaises(ValueError):
            self.api.set_max_default(-2)
            self.api.set_max_default(0)
            self.api.set_max_default(1001)

    def test_suggest(self):
        response = self.api.suggest(s='por', max_results=3, vocabulary='es')
        assert len(response) == 3
        assert isinstance(response, list)
        assert response[1]['word'] == 'porque'

if __name__ == "__main__":
    unittest.main()
