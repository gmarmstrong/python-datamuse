import json
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

SUGGEST_PARAMS = [
    's',
    'max',
    'v'
]


class Datamuse():
    def __init__(self, max_results=100):
        self.api_root = 'https://api.datamuse.com'
        self._validate_max(max_results)
        self.max = max_results


    def __repr__(self):
        return '\n'.join(['{0}: {1}'.format(k,v) for k,v in api.__dict__.items()])


    def _validate_max(self, max_results):
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
        data = response.json()
        return data


    def set_max_default(self, max_results):
        self._validate_max(max_results)
        self.max = max_results


    def words(self, **kwargs):
        '''https://www.datamuse.com/api/
        '''
        self._validate_args(kwargs, WORD_PARAMS)
        if 'max' not in kwargs:
            kwargs.update({'max': self.max})
        return self._get_resource('words', **kwargs)


    def suggest(self, **kwargs):
        '''https://www.datamuse.com/api/
        '''
        self._validate_args(kwargs, SUGGEST_PARAMS)
        return self._get_resource('sug', **kwargs)
