from pathlib import Path

from dilemma.adjective import AdjectiveLemmatizer
from dilemma.adverb import AdverbLemmatizer
from dilemma.corpus import Corpus
from dilemma.noun import NounLemmatizer
from dilemma.verb import VerbLemmatizer

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
        return sorted(set(res), key=len)
    else:
        return res
