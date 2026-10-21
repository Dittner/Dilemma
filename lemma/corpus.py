from pathlib import Path


class Corpus:
    def __init__(self, path: Path) -> None:
        self.words = frozenset(self.load_corpus(path))

    def load_corpus(self, path: Path) -> list[str]:
        res = []
        print(f'Loading and parsing file: {path.as_posix()}')
        with path.open() as f:
            while True:
                row = f.readline()
                if row == '':
                    print('---complete')
                    break
                else:
                    res.append(row.strip().lower())
        return res

    def has(self, word: str) -> bool:
        return word in self.words
