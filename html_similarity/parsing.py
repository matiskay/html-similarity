from io import BytesIO, StringIO

import lxml.html
from lxml.etree import ParserError, XMLSyntaxError, _ElementTree

from html_similarity.exceptions import HtmlParsingError

__all__ = ['parse_html']


def parse_html(document: str | bytes) -> _ElementTree:
    '''
    Parse an HTML document into an lxml tree.

    :param document: html string or bytes
    :return: lxml parsed tree
    :raises HtmlParsingError: if the document cannot be parsed
    '''
    try:
        tree = lxml.html.parse(StringIO(document) if isinstance(document, str) else BytesIO(document))
    except (XMLSyntaxError, ParserError) as e:
        raise HtmlParsingError(f'Failed to parse HTML document: {e}') from e

    # lxml's recovering HTML parser accepts empty/whitespace-only input and
    # returns a tree with no root instead of raising.
    if tree.getroot() is None:
        raise HtmlParsingError('Failed to parse HTML document: document is empty')

    return tree
