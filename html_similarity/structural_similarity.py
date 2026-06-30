import difflib
from io import BytesIO, StringIO

import lxml.html
from lxml.etree import ParserError, XMLSyntaxError, _ElementTree

from html_similarity.exceptions import HtmlParsingError


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
        elif isinstance(el, lxml.html.HtmlProcessingInstruction):
            tags.append('processing-instruction')
        else:
            raise ValueError('Don\'t know what to do with element: {}'.format(el))

    return tags


def structural_similarity(document_1: str | bytes, document_2: str | bytes) -> float:
    """
    Computes the structural similarity between two DOM Trees
    :param document_1: html string or bytes
    :param document_2: html string or bytes
    :return: float
    :raises HtmlParsingError: if either document cannot be parsed
    """
    try:
        tree_1 = lxml.html.parse(StringIO(document_1) if isinstance(document_1, str) else BytesIO(document_1))
        tree_2 = lxml.html.parse(StringIO(document_2) if isinstance(document_2, str) else BytesIO(document_2))
    except (XMLSyntaxError, ParserError) as e:
        raise HtmlParsingError(f'Failed to parse HTML document: {e}') from e

    tags1 = get_tags(tree_1)
    tags2 = get_tags(tree_2)
    diff = difflib.SequenceMatcher(autojunk=False)
    diff.set_seq1(tags1)
    diff.set_seq2(tags2)

    return diff.ratio()
