## EN_LEMMATIZER
A dictionary-based lemmatization for quick lookup of an unknown word.


## What does this module do?
1. Verbs
    + removes plural endings;
    + converts a verb from the past tense to the present tense (including irregular verbs);
    + eliminates the __-ing__ form ending;
    + eliminates the ending __-(e)s__ of the verbs in the third-person singular form;

1. Nouns
	+ convert a noun from the plural to the singular;

1. Adjectives
    + removes the comparative and superlative degrees from adjectives.


## Examples
```py
from lemma.lemmatizer import lemmatize

examples = ['missing', 'lazy', 'buries', 'criteria', 'understood', 'algae']
for e in examples:
    res = lemmatize(e)
    print(f'{e} -> {res}')

"""
>>> missing -> ['miss', 'missing']
>>> lazy -> ['lazy']
>>> buries -> ['bury']
>>> best -> ['good', 'best']
>>> criteria -> ['criterion']
>>> understood -> ['understand']
>>> algae -> ['alga', 'algae']
"""

```

To see more examples, look at the tests:
https://github.com/Dittner/en_lemmatizer/tests/test_lemmatizer.py


## Install
```cmd
pip install git+https://github.com/Dittner/en_lemmatizer
```

## To run locally
```cmd
git clone https://github.com/Dittner/en_lemmatizer
cd <Project-Dir>
uv sync
uv run main.py
pytest 
````

## License
MIT
