from pathlib import Path

from lemma.adjective import AdjectiveLemmatizer
from lemma.adverb import AdverbLemmatizer
from lemma.corpus import Corpus
from lemma.noun import NounLemmatizer
from lemma.verb import VerbLemmatizer

verbs = VerbLemmatizer()
nouns = NounLemmatizer()
adj = AdjectiveLemmatizer()
adverbs = AdverbLemmatizer()
conjunctions_and_prepositions = Corpus(Path(__file__).resolve().parent / 'data/conj_prep.txt')
numbers = Corpus(Path(__file__).resolve().parent / 'data/numbers.txt')


def lemmatize(word: str) -> list[str]:
    if conjunctions_and_prepositions.has(word):
        return [word]

    if numbers.has(word):
        return [word]

    nn = nouns.find(word)
    vv = verbs.find(word)
    ad = adverbs.find(word)
    aa = adj.find(word)

    res = nn + vv + ad + aa

    if len(res) > 1:
        return sorted(set(res), key=lambda item: len(item))
    else:
        return res


# def parse():
#     adjectives_coprus = Corpus(Path(__file__).resolve().parent / 'data/adverbs.txt')
#     top100_coprus = Corpus(Path(__file__).resolve().parent / 'data/conj_prep.txt')
#     unique = top100_coprus.words - adjectives_coprus.words
#     unique_words = sorted(unique)
#     print('Unique words num: ', len(unique_words))
#     for v in unique_words:
#         print(v)
