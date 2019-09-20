[![Build Status](https://travis-ci.org/gmarmstrong/python-datamuse.svg?branch=master)](https://travis-ci.org/gmarmstrong/python-datamuse)

# python-datamuse

Python wrapper and scripts for the [Datamuse API](http://datamuse.com/api/).
Available on PyPI at <https://pypi.python.org/pypi/python-datamuse>. You can
install this library with `pip3 install python-datamuse`.

## Changelog

### Version 1.3.0

- Add optional arguments to `suggest` method

### Version 1.2.1

- Fix README formatting on PyPI

### Version 1.2.0

- Raise Python version to 3.6
- Mock the Datamuse API for tests
- Restructure project files
- Set README as PyPI long description

### Version 1.1.0

- Changed to Python 3
- Uploaded to PyPI, added instructions for PyPI installation
- Changed README example to reflect PyPI packaging
- Set up Travis CI
- Temporarily removed pandas
- Changed mode of scripts to executable

## Example

```python
>>> from datamuse import datamuse
>>> api = datamuse.Datamuse()
>>> ninth_rhymes = api.words(rel_rhy='ninth', max=5)
>>> ninth_rhymes
[]
>>> orange_rhymes = api.words(rel_rhy='orange', max=5)
>>> orange_rhymes
[{'word': 'door hinge', 'score': 74, 'numSyllables': 2}]
>>> yellow_things = api.words(rel_jja='yellow', max=5)
>>> yellow_things
[{'word': 'fever', 'score': 1001}, {'word': 'color', 'score': 1000}, {'word': 'flowers', 'score': 999}, {'word': 'light', 'score': 998}, {'word': 'colour', 'score': 997}]
>>> foo_complete = api.suggest(s='foo', max=10)
>>> foo_complete
[{'word': 'food', 'score': 3888}, {'word': 'foot', 'score': 3041}, {'word': 'fool', 'score': 1836}, {'word': 'football', 'score': 1424}, {'word': 'footage', 'score': 1328}, {'word': 'footprint', 'score': 1082}, {'word': 'foolish', 'score': 967}, {'word': 'foof', 'score': 930}, {'word': 'footing', 'score': 786}, {'word': 'foolproof', 'score': 697}]
```

Note that the default number of results is set to 100. You can set the default
`max` to something else using the `set_max_default` method, e.g.
`api.set_max_default(300)`. Datamuse only returns 1000 results max.
