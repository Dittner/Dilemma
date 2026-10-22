## Intro
A dictionary-based lemmatization for quick lookup of an unknown word (English only).


## Features
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
from dilemma.lemmatizer import lemmatize

examples = ['missing', 'lazy', 'buries', 'best', 'criteria', 'understood', 'algae']
for e in examples:
    res = lemmatize(e)
    print(f'{e} -> {res}')
```
Output:
```terminal
missing -> ['miss', 'missing'] # 'missing' can be a verb 'sing' with a prefix 'mis'
lazy -> ['lazy']
buries -> ['bury']
best -> ['good', 'best'] # 'best' can be a verb
criteria -> ['criterion']
understood -> ['understand']
algae -> ['alga', 'algae']
```

To see more examples, look at the tests:
https://github.com/Dittner/Dilemma/blob/main/tests/test_lemmatizer.py


## Install
```bash
pip install "git+https://github.com/Dittner/Dilemma"
```
or
```bash
uv add "git+https://github.com/Dittner/Dilemma"
```

## To run locally
```bash
git clone https://github.com/Dittner/Dilemma
cd Dilemma
uv sync
uv run main.py
uv run pytest tests/test_lemmatizer.py
```

## License
MIT
