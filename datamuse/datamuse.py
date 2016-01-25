import json
import requests

class Datamuse():
    def __init__(self):
        self.api_root = 'https://api.datamuse.com'
        self.word_params = {
            'ml',
            'sl',
            'sp',
            'rel_jja',
            'rel_jjb',
            'rel_syn',
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
            'max'
        }
        self.suggest_params = {
            's',
            'max',
            'v'
        }

    def validate_args(self, args, param_set):
        for arg in args:
            if arg not in param_set:
                raise ValueError('{0} is not a valid parameter for this endpoint.'.format(arg))

    def get_resource(self, endpoint, **kwargs):
        # I feel like this should have some kind of error handling...
        url = self.api_root + endpoint
        response = requests.get(url, params=kwargs)
        data = response.json()
        return data

    def words(self, **kwargs):
        self.validate_args(kwargs, self.word_params)
        words = '/words'
        return self.get_resource(words, **kwargs)

    def suggest(self, **kwargs):
        self.validate_args(kwargs, self.suggest_params)
        sug = '/sug'
        return self.get_resource(sug, **kwargs)