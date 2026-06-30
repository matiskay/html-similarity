from lxml.etree import _ElementTree
from rapidfuzz.distance import Indel

from html_similarity.algorithms.common import get_tags


def similarity(tree_1: _ElementTree, tree_2: _ElementTree) -> float:
    '''
    Flat tag-sequence comparison via rapidfuzz's bit-parallel Indel/LCS implementation.
    Fastest option, but blind to nesting changes that don't alter the DFS tag order.
    '''
    return Indel.normalized_similarity(get_tags(tree_1), get_tags(tree_2))
