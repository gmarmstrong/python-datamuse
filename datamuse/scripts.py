import pandas as pd

def dm_to_df(datamuse_response):
    """Converts the json response of the datamuse API into a DataFrame
    :datamuse_response
        [{'word': 'foo', 'score': 100}, {'word': 'bar', 'score': 120}]
    """
    reformatted = {
        'word': [],
        'score': []
    }
    for result in datamuse_response:
        reformatted['word'].append(result['word'])
        reformatted['score'].append(result['score'])
    return pd.DataFrame.from_dict(reformatted)