===============
HTML Similarity
===============

.. image:: https://travis-ci.org/matiskay/html-similarity.svg?branch=master
    :target: https://travis-ci.org/matiskay/html-similarity

.. image:: https://codebeat.co/badges/304915eb-48a3-46a8-9ce9-2790c82dc2b8
    :target: https://codebeat.co/projects/github-com-matiskay-html-similarity-master

This package provides a set of functions to measure the similarity between web pages.

Install
=======

The quick way::

    pip install html-similarity

How it works?
=============

Structural Similarity
---------------------

Uses sequence comparison of the html tags to compute the similarity.

We not implement the similarity based on tree edit distance because it is slower than sequence comparison.


Style Similarity
----------------

Extracts css classes of each html document and calculates the jaccard similarity of the sets of classes.


Joint Similarity (Structural Similarity and Style Similarity)
-------------------------------------------------------------

The joint similarity metric is calculated as::

    k * structural_similarity(document_1, document_2) + (1 - k) * style_similarity(document_1, document_2)


All the similarity metrics takes values between 0 and 1.

Recommendations for joint similarity
------------------------------------

Using `k=0.3` give use better results. The style similarity gives more information about the similarity rather than the structural similarity.

Examples
========

Here is a example::

    In [1]: html_1 = '''
    <h1 class="title">First Document</h1>
    <ul class="menu">
        <li class="active">Documents</li>
        <li>Extra</li>
    </ul>
    '''

    In [2]: html_2 = '''
    <h1 class="title">Second document Document</h1>
    <ul class="menu">
        <li class="active">Extra Documents</li>
    </ul>
    '''

    In [3] from html_similarity import style_similarity, structural_similarity, similarity

    In [4]: style_similarity(html_1, html_2)
    Out[4]: 1.0

    In [7]: structural_similarity(html_1, html_2)
    Out[7]: 0.9090909090909091

    In [8]: similarity(html_1, html_2)
    Out[8]: 0.9545454545454546

References
==========

- The idea of sequence comparision was taken from `Page Compare <https://github.com/TeamHG-Memex/page-compare>`_.
- The other ideas were taken from `T. Gowda and C. A. Mattmann, Clustering Web Pages Based on Structure and Style Similarity, 2016 IEEE 17th International Conference on Information Reuse and Integration (IRI), Pittsburgh, PA, 2016, pp. 175-180. <http://ieeexplore.ieee.org/document/7785739/>`_
- Use case `Clustering web pages based on structure and style similarity <https://www.slideshare.net/thammegowda/ieee-iri-16-clustering-web-pages-based-on-structure-and-style-similarity?qid=7deea5f8-157d-4e57-a413-16ec7c6a22d9&v=&b=&from_search=1>`_
