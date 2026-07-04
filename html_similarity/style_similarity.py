from collections.abc import Iterable

from lxml.etree import _ElementTree

from html_similarity.parsing import parse_html


def get_classes(document: str | bytes | _ElementTree) -> set[str]:
    '''
    Extract the set of CSS class names used in a document.

    Walks the tree directly instead of using an XPath query: the equivalent
    ``//*[@class]/@class`` query degrades superlinearly on large documents,
    while this walk stays linear.

    :param document: html string, bytes, or an already-parsed lxml tree
    :return: set of CSS class names
    :raises HtmlParsingError: if the document cannot be parsed
    '''
    tree = document if isinstance(document, _ElementTree) else parse_html(document)
    result: set[str] = set()
    for el in tree.getroot().iter():
        classes = el.get('class')
        if classes:
            result.update(classes.split())
    return result


def jaccard_similarity(set1: Iterable[str], set2: Iterable[str]) -> float:
    set1 = set(set1)
    set2 = set(set2)
    intersection = len(set1 & set2)

    if len(set1) == 0 and len(set2) == 0:
        return 1.0

    denominator = len(set1) + len(set2) - intersection
    return intersection / max(denominator, 0.000001)


def style_similarity(page1: str | bytes, page2: str | bytes) -> float:
    """
    Computes CSS style Similarity between two DOM trees

    A = classes(Document_1)
    B = classes(Document_2)

    style_similarity = |A & B| / (|A| + |B| - |A & B|)

    :param page1: html of the page1
    :param page2: html of the page2
    :return: Number between 0 and 1. If the number is next to 1 the page are really similar.
    :raises HtmlParsingError: if either document cannot be parsed
    """
    classes_page1 = get_classes(page1)
    classes_page2 = get_classes(page2)
    return jaccard_similarity(classes_page1, classes_page2)
