import pandas as pd

def dm_to_df(datamuse_response):
    """Converts the json response of the datamuse API into a DataFrame
    :datamuse_response
        [{'word': 'foo', 'score': 100}, {'word': 'bar', 'score': 120}]
    """
    reformatted = {
        'word': [response['word'] for response in datamuse_response],
        'score': [response['score'] for response in datamuse_response]
    }
    return pd.DataFrame.from_dict(reformatted)