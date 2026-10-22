"""
Lemmatizer

A vocabulary-based, fast English lemmatizer.
"""

from .corpus import Corpus
from .lemmatizer import get_past_and_perfect_form, lemmatize
from .noun import NounLemmatizer
from .verb import VerbLemmatizer

__version__ = '0.3.1'
__all__ = ['Corpus', 'NounLemmatizer', 'VerbLemmatizer', 'get_past_and_perfect_form', 'lemmatize']
