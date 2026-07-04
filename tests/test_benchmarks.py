'''
Regression benchmarks for the public similarity functions.

Run with ``pytest tests/test_benchmarks.py``; pytest-benchmark prints a timing
table. The documents are synthetic but shaped like real pages (wide sibling
lists of classed elements), which is exactly the shape that made the old
XPath-based class extraction degrade superlinearly.
'''

import pytest

from html_similarity import similarity, structural_similarity, style_similarity


def make_document(n_items: int, seed: int) -> str:
    sections = []
    for i in range(n_items):
        variant = (i + seed) % 7
        sections.append(
            f'<div class="card card-{variant}">'
            f'<h2 class="title">Item {i}</h2>'
            f'<p class="body text-{variant}">text</p>'
            '</div>'
        )
    return f'<html><body class="page"><main class="content">{"".join(sections)}</main></body></html>'


@pytest.fixture(scope='module')
def documents() -> tuple[str, str]:
    return make_document(1000, seed=0), make_document(1000, seed=3)


def test_benchmark_similarity(benchmark, documents):
    result = benchmark(similarity, *documents)
    assert 0.0 <= result <= 1.0


def test_benchmark_structural_similarity(benchmark, documents):
    result = benchmark(structural_similarity, *documents)
    assert 0.0 <= result <= 1.0


def test_benchmark_style_similarity(benchmark, documents):
    result = benchmark(style_similarity, *documents)
    assert 0.0 <= result <= 1.0
