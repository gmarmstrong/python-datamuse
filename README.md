# python-datamuse
Basic Python wrapper and scripts for the Datamuse API. Everything is in a single directory because I'm too lazy to figure out how to do the relative imports properly right now. Same for why it's in Python 2 instead of 3 (getting tests and libraries to work for both). 

Docs at http://datamuse.com/api/

## Example
```
>>> from datamuse import Datamuse
>>> api = Datamuse()
>>> orange_rhymes = api.words(rel_rhy='orange', max=5)
>>> orange_rhymes
[]
>>> orange_near_rhymes = api.words(rel_nry='orange', max=5)
>>> orange_near_rhymes
[{'score': 973, 'word': 'storage'}, {'score': 858, 'word': 'knowledge'}, {'score': 615, 'word': 'homage'}, {'score': 560, 'word': 'warrant'}]
>>> foo_complete = api.suggest(s='foo', max=10)
>>> foo_complete
[{u'score': 626, u'word': u'food'}, {u'score': 568, u'word': u'foot'}, {u'score': 520, u'word': u'fool'}, {u'score': 315, u'word': u'footage'}, {u'score': 297, u'word': u'foolish'}, {u'score': 279, u'word': u'football'}, {u'score': 272, u'word': u'footprint'}, {u'score': 232, u'word': u'footing'}, {u'score': 221, u'word': u'foof'}, {u'score': 185, u'word': u'foolproof'}]
```

## To Do
* Can this work in Python 2 and 3?
* More scripts to do interesting things. 
* Not sure whether I should move the pandas stuff into the Datamuse class or keep it separate in case you don't need pandas for whatever you're doing with this. 