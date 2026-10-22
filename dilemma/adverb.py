from pathlib import Path

from dilemma.corpus import Corpus


class AdverbLemmatizer:
    def __init__(self) -> None:
        path = Path(__file__).resolve().parent / 'data/adverbs.txt'
        self.corpus = Corpus(path)

    def find(self, word: str) -> list[str]:
        if self.corpus.has(word):
            return [word]
        else:
            return []
