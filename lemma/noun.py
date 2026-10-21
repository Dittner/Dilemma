import re
from pathlib import Path

from lemma.corpus import Corpus

pl_to_sg_exclusions = {
    'mice': 'mouse',
    'lice': 'louse',
    'geese': 'goose',
    'phenomena': 'phenomenon',
    'criteria': 'criterion',
    'nuclei': 'nucleus',
    'radii': 'radius',
    'cacti': 'cactus',
    'memoranda': 'memorandum',
    'curricula': 'curriculum',
    'genera': 'genus',
    'corpora': 'corpus',
}


class NounLemmatizer:
    def __init__(self) -> None:
        path = Path(__file__).resolve().parent / 'data/nouns.txt'
        self.corpus = Corpus(path)
        self.patterns = [
            # plural
            (r'^([a-zA-Z]+(s|ss|sh|ch|x|z))es$', lambda res: res[0]),  # boxes -> box
            (r'^([a-zA-Z]+)ies$', lambda res: res + 'y'),  # babies -> baby
            (r'^([a-zA-Z]+)ves$', lambda res: res + 'fe'),  # wives -> wife
            (r'^([a-zA-Z]+)ves$', lambda res: res + 'f'),  # leaves -> leaf
            (r'^([a-zA-Z]+o)es$', None),  # potato -> potatoes
            (r'^([a-zA-Z]+)men$', lambda res: res + 'man'),  # women -> woman
            (r'^([a-zA-Z]*child)ren$', None),  # godchildren -> godchild
            (r'^([a-zA-Z]*)feet$', lambda res: res + 'foot'),
            (r'^([a-zA-Z]*)teeth$', lambda res: res + 'tooth'),
            (r'^([a-zA-Z]+a)e$', None),  # lat. nebulae -> nebula
            (r'^([a-zA-Z]+i)ces$', lambda res: res + 'x'),  # lat. matrices -> matrix
            (r'^([a-zA-Z]+)ices$', lambda res: res + 'ex'),  # lat. vertices -> vertex
            (r'^([a-zA-Z]+ri)a$', lambda res: res + 'um'),  # lat. bacteria -> bacterium
            (r'^([a-zA-Z]+)s$', None),
        ]

    def find(self, word: str) -> list[str]:
        res = []

        ex_word = pl_to_sg_exclusions.get(word)
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
