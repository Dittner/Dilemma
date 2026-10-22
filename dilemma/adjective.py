import re
from pathlib import Path

from dilemma.corpus import Corpus

exclusions = {
    'better': 'good',
    'best': 'good',
    'worse': 'bad',
    'worst': 'bad',
    'farther': 'far',
    'farthest': 'far',
    'further': 'far',
    'furthest': 'far',
    'less': 'little',
    'least': 'little',
    'more': 'many',
    'most': 'many',
    'elder': 'old',
    'eldest': 'old',
    'oldest': 'old',
}


class AdjectiveLemmatizer:
    def __init__(self) -> None:
        path = Path(__file__).resolve().parent / 'data/adjectives.txt'
        self.corpus = Corpus(path)
        self.patterns = [
            # comparative
            (r'^([a-zA-Z]+)ier$', lambda res: res + 'y'),  # happier -> happy
            (r'^([a-zA-Z]+(bb|dd|ff|gg|mm|nn|pp|rr|tt|ll))er$', lambda res: res[0][:-1]),  # bigger -> big
            (r'^([a-zA-Z]+e)r$', None),  # nicer -> nice
            (r'^([a-zA-Z]+)er$', None),  # faster -> fast
            # superlative
            (r'^([a-zA-Z]+)iest$', lambda res: res + 'y'),  # prettiest -> pretty
            (r'^([a-zA-Z]+(bb|dd|ff|gg|mm|nn|pp|rr|tt|ll))est$', lambda res: res[0][:-1]),  # thinnest -> thin
            (r'^([a-zA-Z]+e)st$', None),  # bravest -> brave
            (r'^([a-zA-Z]+)est$', None),  # fastest -> fast
        ]

    def find(self, word: str) -> list[str]:
        res = []

        ex_word = exclusions.get(word)
        if ex_word:
            res.append(ex_word)

        if self.corpus.has(word):
            res.append(word)

        for pattern, post_handler in self.patterns:
            matches = re.findall(pattern, word)
            if len(matches) > 0:
                m = matches[0]
                if post_handler:
                    m = post_handler(m)
                if self.corpus.has(m):
                    res.append(m)

        return res
