"""
Lemmatizer

A vocabulary-based, fast English lemmatizer.
"""

from .corpus import Corpus
from .lemmatizer import lemmatize
from .noun import NounLemmatizer
from .verb import VerbLemmatizer

__version__ = '0.0.1'
__all__ = ['Corpus', 'NounLemmatizer', 'VerbLemmatizer', 'lemmatize']
