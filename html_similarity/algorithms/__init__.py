from collections.abc import Callable
from enum import Enum

from lxml.etree import _ElementTree

from html_similarity.algorithms import difflib_algorithm, indel, pq_gram


class StructuralAlgorithm(str, Enum):
    '''Available algorithms for :func:`html_similarity.structural_similarity.structural_similarity`.'''

    INDEL = 'indel'
    PQ_GRAM = 'pq_gram'
    DIFFLIB = 'difflib'


ALGORITHMS: dict[StructuralAlgorithm, Callable[[_ElementTree, _ElementTree], float]] = {
    StructuralAlgorithm.INDEL: indel.similarity,
    StructuralAlgorithm.PQ_GRAM: pq_gram.similarity,
    StructuralAlgorithm.DIFFLIB: difflib_algorithm.similarity,
}

DEFAULT_ALGORITHM = StructuralAlgorithm.INDEL

__all__ = ['StructuralAlgorithm', 'ALGORITHMS', 'DEFAULT_ALGORITHM']
