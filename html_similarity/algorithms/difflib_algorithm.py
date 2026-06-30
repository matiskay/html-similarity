import difflib

from lxml.etree import _ElementTree

from html_similarity.algorithms.common import get_tags


def similarity(tree_1: _ElementTree, tree_2: _ElementTree) -> float:
    '''
    Legacy flat tag-sequence comparison (the original implementation), kept for
    benchmarking against indel. O(n*m) worst case, which large repetitive
    documents hit often.
    '''
    diff = difflib.SequenceMatcher(autojunk=False)
    diff.set_seq1(get_tags(tree_1))
    diff.set_seq2(get_tags(tree_2))
    return diff.ratio()
