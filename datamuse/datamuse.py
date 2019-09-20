#!/usr/bin/env python3

import requests

WORD_PARAMS = [
    'ml',
    'sl',
    'sp',
    'rel_jja',
    'rel_jjb',
    'rel_syn',
    'rel_trg',
    'rel_ant',
    'rel_spc',
    'rel_gen',
    'rel_com',
    'rel_par',
    'rel_bga',
    'rel_bgb',
    'rel_rhy',
    'rel_nry',
    'rel_hom',
    'rel_cns',
    'v',
    'topics',
    'lc',
    'rc',
    'max',
    'md',
    'qe'
]


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

    def _validate_args(self, args, param_set):
        for arg in args:
            if arg not in param_set:
                raise ValueError('{0} is not a valid parameter for this endpoint.'.format(arg))
            if arg == 'max':
                self._validate_max(args[arg])

    def _get_resource(self, endpoint, **kwargs):
        url = '/'.join([self.api_root, endpoint])
        response = requests.get(url, params=kwargs)
        return response.json()

    def set_max_default(self, max_results):
        self._validate_max(max_results)
        self.max = max_results

    def words(self, **kwargs):
        """https://www.datamuse.com/api/"""
        self._validate_args(kwargs, WORD_PARAMS)
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
