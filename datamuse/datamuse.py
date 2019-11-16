#!/usr/bin/env python3

import requests


class Datamuse(object):

    def __init__(self, max_results=100):
        self.api_root = 'https://api.datamuse.com'
        self._validate_max(max_results)
        self.max = max_results

    def __repr__(self):
        return '\n'.join(['{0}: {1}'.format(k, v) for k, v in requests.api.__dict__.items()])

    @staticmethod
    def _validate_max(max_results):
        if not (0 < max_results <= 1000):
            raise ValueError("Datamuse only supports values of max in (0, 1000]")

    def _get_resource(self, endpoint, **kwargs):
        url = '/'.join([self.api_root, endpoint])
        response = requests.get(url, params=kwargs)
        return response.json()

    def set_max_default(self, max_results):
        self._validate_max(max_results)
        self.max = max_results

    def words(self, **kwargs):
        """
        This endpoint returns a list of words (and multiword expressions) from
        a given vocabulary that match a given set of constraints.

        See <https://www.datamuse.com/api/> for the official Datamuse API
        documentation for the `/words` endpoint.

        :param `**kwargs`: Query parameters of constraints and hints.
        :return: A list of words matching that match the given constraints.
        """
        if 'max' not in kwargs:
            kwargs.update({'max': self.max})
        return self._get_resource('words', **kwargs)

    def suggest(self, s, max_results=None, vocabulary=None):
        """
        This resource is useful as a backend for “autocomplete” widgets
        on websites and apps when the vocabulary of possible search terms
        is very large.

        It provides word suggestions given a partially-entered query
        using a combination of the operations.

        The suggestions perform live spelling correction and intelligently
        fall back to choices that are phonetically or semantically similar
        when an exact prefix match can't be found.

        :param s: Prefix hint string; typically, the characters that
            the user has entered so far into a search box.
        :param max_results: Maximum number of results to return, not to exceed 1000.
        :param vocabulary: The language vocabulary to use. Currently, `en` and `es` are supported.
        :return: A list of suggested words to the given string s.
        """
        payload = {'s': s}
        if max_results is not None:
            payload['max'] = max_results
        if vocabulary is not None:
            payload['v'] = vocabulary
        return self._get_resource('sug', **payload)
