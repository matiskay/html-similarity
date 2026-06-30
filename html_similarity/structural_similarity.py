from io import BytesIO, StringIO

import lxml.html
from lxml.etree import ParserError, XMLSyntaxError

from html_similarity.algorithms import ALGORITHMS, DEFAULT_ALGORITHM, StructuralAlgorithm
from html_similarity.exceptions import HtmlParsingError

__all__ = ['structural_similarity', 'StructuralAlgorithm']


def structural_similarity(
    document_1: str | bytes,
    document_2: str | bytes,
    algorithm: StructuralAlgorithm | str = DEFAULT_ALGORITHM,
) -> float:
    """
    Computes the structural similarity between two DOM Trees

    :param document_1: html string or bytes
    :param document_2: html string or bytes
    :param algorithm: comparison algorithm to use, see html_similarity.algorithms.StructuralAlgorithm:
        - ``indel`` (default): fastest, flat tag-sequence comparison via rapidfuzz's
          bit-parallel Indel/LCS implementation.
        - ``pq_gram``: tree-structure aware, approximates Tree Edit Distance by
          comparing pq-gram profiles instead of a flat sequence.
        - ``difflib``: legacy flat tag-sequence comparison, kept for benchmarking.
    :return: float
    :raises HtmlParsingError: if either document cannot be parsed
    """
    algorithm = StructuralAlgorithm(algorithm)

    try:
        tree_1 = lxml.html.parse(StringIO(document_1) if isinstance(document_1, str) else BytesIO(document_1))
        tree_2 = lxml.html.parse(StringIO(document_2) if isinstance(document_2, str) else BytesIO(document_2))
    except (XMLSyntaxError, ParserError) as e:
        raise HtmlParsingError(f'Failed to parse HTML document: {e}') from e

    return ALGORITHMS[algorithm](tree_1, tree_2)
