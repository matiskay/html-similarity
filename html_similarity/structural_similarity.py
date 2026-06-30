import difflib
from io import StringIO

import lxml.html
from lxml.etree import _ElementTree


def get_tags(doc: _ElementTree) -> list[str]:
    '''
    Get tags from a DOM tree

    :param doc: lxml parsed object
    :return:
    '''
    tags: list[str] = []

    for el in doc.getroot().iter():
        if isinstance(el, lxml.html.HtmlElement):
            tags.append(el.tag)
        elif isinstance(el, lxml.html.HtmlComment):
            tags.append('comment')
        else:
            raise ValueError('Don\'t know what to do with element: {}'.format(el))

    return tags


def structural_similarity(document_1: str, document_2: str) -> float:
    """
    Computes the structural similarity between two DOM Trees
    :param document_1: html string
    :param document_2: html string
    :return: int
    """
    try:
        tree_1 = lxml.html.parse(StringIO(document_1))
        tree_2 = lxml.html.parse(StringIO(document_2))
    except Exception as e:
        print(e)
        return 0

    tags1 = get_tags(tree_1)
    tags2 = get_tags(tree_2)
    diff = difflib.SequenceMatcher()
    diff.set_seq1(tags1)
    diff.set_seq2(tags2)

    return diff.ratio()
