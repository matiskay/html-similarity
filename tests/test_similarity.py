from html_similarity import style_similarity
from html_similarity.style_similarity import jaccard_similarity
from html_similarity import structural_similarity

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

xhtml_1 = '''
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

xhtml_2 = '''
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

def test_bytes_similarity():
    assert 1 == structural_similarity(xhtml_1.encode('utf-8'), xhtml_2.encode('utf-8'))
