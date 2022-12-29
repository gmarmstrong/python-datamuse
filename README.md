# python-datamuse

[![PyPI](https://img.shields.io/pypi/v/python-datamuse)](https://pypi.org/project/python-datamuse/)
[![PyPI - License](https://img.shields.io/pypi/l/python-datamuse)](https://github.com/gmarmstrong/python-datamuse/blob/main/LICENSE)
[![CodeQL](https://github.com/gmarmstrong/python-datamuse/actions/workflows/codeql-analysis.yml/badge.svg?branch=main)](https://github.com/gmarmstrong/python-datamuse/actions/workflows/codeql-analysis.yml)

Python wrapper and scripts for the [Datamuse API](http://datamuse.com/api/).
Available on PyPI at <https://pypi.python.org/pypi/python-datamuse>. You can
install this library with `pip3 install python-datamuse`.

## Changelog

### Version 2.0.* (2022-10-22)

- require Python 3.7
- add @margaret to authors
- upgrade trove classifier "Development Status" from "3 - Alpha" to "5 - Production/Stable"
- specify all dependency version requirements
- rename default branch `main`
- build tool changes, see <https://github.com/gmarmstrong/python-datamuse/releases/tag/v2.0.0>
- **(2.0.1) (2022-12-29):** fix CI workflows

### Version 1.3.* (2019-09-20)

- Add optional arguments to `suggest` method
- Document and test suggestion method
- **(1.3.1):** Update README example
- **(1.3.1):** Remove WORD_PARAMS
- **(1.3.1):** Document `words` method
- **(1.3.2) (2022-04-04):** Fix test_set_max bug 

### Version 1.2.* (2018-10-23)

- Raise Python version to 3.6
- Mock the Datamuse API for tests
- Restructure project files
- Set README as PyPI long description
- **(1.2.1):** Fix README formatting on PyPI

### Version 1.1.0 (2018-02-18)

- Changed to Python 3
- Uploaded to PyPI, added instructions for PyPI installation
- Changed README example to reflect PyPI packaging
- Set up Travis CI
- Temporarily removed pandas
- Changed mode of scripts to executable

## Example

```
>>> from datamuse import Datamuse
>>> api = Datamuse()
>>> api.words(rel_rhy='ninth', max=5)  # words that rhyme with "ninth"
[]
>>> api.words(rel_rhy='orange', max=5)  # words that rhyme with "orange"
[{'word': 'door hinge', 'score': 74, 'numSyllables': 2}]
>>> api.words(rel_jja='yellow', max=5)  # things often described as "yellow"
[{'word': 'fever', 'score': 1001}, {'word': 'color', 'score': 1000}, {'word': 'flowers', 'score': 999}, {'word': 'light', 'score': 998}, {'word': 'colour', 'score': 997}]
>>> api.suggest(s='foo', max_results=10)  # completion suggestions for "foo"
[{'word': 'food', 'score': 3888}, {'word': 'foot', 'score': 3041}, {'word': 'fool', 'score': 1836}, {'word': 'football', 'score': 1424}, {'word': 'footage', 'score': 1328}, {'word': 'footprint', 'score': 1082}, {'word': 'foolish', 'score': 967}, {'word': 'foof', 'score': 930}, {'word': 'footing', 'score': 786}, {'word': 'foolproof', 'score': 697}]
```

Note that the default number of results is set to 100. You can set the default
`max` to something else using the `set_max_default` method, e.g.
`api.set_max_default(300)`. Datamuse only returns 1000 results max.
