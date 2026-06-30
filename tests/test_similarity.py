from unittest.mock import patch

import lxml.html
import pytest
from lxml import etree

from html_similarity import HtmlParsingError, structural_similarity, style_similarity
from html_similarity.structural_similarity import get_tags
from html_similarity.style_similarity import jaccard_similarity

from .utils import almost_equal


html1 = ''''
<html>
    <body class="body-class">
        <h1 class="title">This a title<h1>
        <ul>
            <li class="item active">item 1</li>
            <li class="item">item 2</li>
            <li class="item">item 3</li>
        <ul>
    </body>
</html>
'''

html2 = ''''
<html>
    <body class="body-class">
        <h2 class="title">This a title<h2>
        <ul>
            <li class="item">item 1</li>
            <li class="item">item 2</li>
            <li class="item active">item 3</li>
        <ul>
    </body>
</html>
'''


def test_style_similarity():
    assert 1 == style_similarity(html1, html2)


def test_no_styles_similarity():
    assert 1 == style_similarity('<h1>No class here</h1>', '<h1>Look no css class here</h1>')


def test_jaccard_similarity():
    assert 1 == jaccard_similarity(['a', 'b', 'c'], ['a', 'b', 'c'])
    assert almost_equal(0.6666, jaccard_similarity(['a', 'b'], ['a', 'b', 'c']))
    assert 0 == jaccard_similarity(['d', 'e'], ['a', 'b', 'c'])
    assert almost_equal(jaccard_similarity(list(range(1, 1000000)), list(range(1000000 - 10, 2 * 1000000))), 0)


xhtml1 = '''
<?xml version="1.0" encoding="UTF-8" ?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html>
    <body class="body-class">
        <h1 class="title">This a title<h1>
        <ul>
            <li class="item active">item 1</li>
            <li class="item">item 2</li>
            <li class="item">item 3</li>
        <ul>
    </body>
</html>
'''

xhtml2 = '''
<?xml version="1.0" encoding="UTF-8" ?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html>
    <body class="body-class">
        <h1 class="title">This a different title<h1>
        <ul>
            <li class="item active">item 1</li>
            <li class="item">item 2</li>
            <li class="item">item 3</li>
        <ul>
    </body>
</html>
'''


def test_structural_similarity_from_bytes():
    assert 1 == structural_similarity(xhtml1.encode('utf-8'), xhtml2.encode('utf-8'))


def test_get_tags_with_processing_instruction():
    root = lxml.html.fromstring('<html><body><h1 class="title">hi</h1></body></html>')
    root.find('body').insert(0, lxml.html.HtmlProcessingInstruction('php', 'echo 1;'))

    tags = get_tags(etree.ElementTree(root))

    assert tags == ['html', 'body', 'processing-instruction', 'h1']


def test_structural_similarity_ignores_autojunk_on_large_repetitive_documents():
    # difflib.SequenceMatcher's default autojunk=True treats elements occurring
    # in >1% of positions as "popular" and excludes them from matching once a
    # sequence has >=200 items. Long HTML documents are dominated by a handful
    # of repeated tags (div, li, span, ...), which is exactly this case, so the
    # default would badly understate similarity between near-identical pages.
    def make_html(n, first_tag):
        body = f'<{first_tag}>x</{first_tag}>' + '<div>x</div>' * (n - 1)
        return f'<html><body>{body}</body></html>'

    doc1 = make_html(250, 'div')
    doc2 = make_html(250, 'span')  # differs in exactly 1 of 251 tags

    assert almost_equal(structural_similarity(doc1, doc2), 250 / 251, threshold=0.01)


def test_structural_similarity_raises_html_parsing_error_on_xml_syntax_error():
    with patch('lxml.html.parse', side_effect=etree.XMLSyntaxError('boom', 0, 0, 0)):
        with pytest.raises(HtmlParsingError):
            structural_similarity('<html></html>', '<html></html>')


def test_structural_similarity_raises_html_parsing_error_on_parser_error():
    with patch('lxml.html.parse', side_effect=etree.ParserError('boom')):
        with pytest.raises(HtmlParsingError):
            structural_similarity('<html></html>', '<html></html>')
