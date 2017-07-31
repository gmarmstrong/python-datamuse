# python-datamuse

Basic Python (2) wrapper and scripts for the Datamuse API. I'm not associated with Datamuse or OneLook, but I thought the API looked interesting and spun this up to make querying it a bit easier.

Docs at http://datamuse.com/api/

## Dependencies

This API requires the `requests` library. You can install the requests module with the command `pip install -r requirements.txt`.

If you want to use the `dm_to_df` function in `datamuse/scripts.py`, you'll also need to install pandas separately, but presumably if you're going to use that you've got pandas installed already.

## Example

Assuming this is run from the top level directory
```python
>>> from datamuse import datamuse
>>> api = datamuse.Datamuse()
>>> orange_rhymes = api.words(rel_rhy='orange', max=5)
>>> orange_rhymes
[]
>>> orange_near_rhymes = api.words(rel_nry='orange', max=5)
>>> orange_near_rhymes
[{'score': 973, 'word': 'storage'}, {'score': 858, 'word': 'knowledge'}, {'score': 615, 'word': 'homage'}, {'score': 560, 'word': 'warrant'}]
>>>
>>>
>>> foo_complete = api.suggest(s='foo', max=10)
>>> foo_complete
[{u'score': 626, u'word': u'food'}, {u'score': 568, u'word': u'foot'}, {u'score': 520, u'word': u'fool'}, {u'score': 315, u'word': u'footage'}, {u'score': 297, u'word': u'foolish'}, {u'score': 279, u'word': u'football'}, {u'score': 272, u'word': u'footprint'}, {u'score': 232, u'word': u'footing'}, {u'score': 221, u'word': u'foof'}, {u'score': 185, u'word': u'foolproof'}]
>>> from datamuse import scripts
>>> foo_df = scripts.dm_to_df(foo_complete)
>>> foo_df
   score       word
0    626       food
1    568       foot
2    521       fool
3    315    footage
4    297    foolish
5    279   football
6    272  footprint
7    232    footing
8    221       foof
9    185  foolproof

[10 rows x 2 columns]
```

Note that the default number of results is set to 100. You can set the default `max` to something else using the `set_max_default` method, e.g. `api.set_max_default(300)`. Datamuse only returns 1000 results max.

## To Do

* Add support for Python 3
* Add CI
* Proper pacakging setup
