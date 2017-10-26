from pytest import approx

from html_similarity import style_similarity
from html_similarity.style_similarity import jaccard_similarity


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


def test_jaccard_similarity():
    assert 1 == jaccard_similarity(['a', 'b', 'c'], ['a', 'b', 'c'])
    assert approx(0.666, jaccard_similarity(['a', 'b'], ['a', 'b', 'c']))
