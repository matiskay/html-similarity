===============
HTML Similarity
===============

.. image:: https://travis-ci.org/matiskay/html-similarity.svg?branch=master
    :target: https://travis-ci.org/matiskay/html-similarity

This package provides a set of functions to measure the similarity between web pages.

Install
=======

The quick way::

    pip install html-similarity

How it works?
=============

Structural Similarity
---------------------

We use sequence comparison fo the html tags to compute the structural similarity instead of
tree edit distance because tree edit distance is slower than sequence comparison.

The idea of sequence comparison was taken from `Page Compare <https://github.com/TeamHG-Memex/page-compare>`_.


Style Similarity
----------------

Extracts css classes of each html document and calculates the jaccard similarity of the sets of classes.
The idea was taken from [1]_


Joint Similarity (Structural Similarity and Style Similarity)
-------------------------------------------------------------

The joint similarity metric is calculated as::

    k * structural_similarity(document_1, document_2) + (1 - k) * style_similarity(document_1, document_2)

This was taken from [1]_

The value is in the interval of 0 and 1.

Recommendations for joint similarity
------------------------------------

Using `k=0.3` give use better results. The style similarity can gives more information
about the similarity rather than the style.


References
==========

.. [1] `T. Gowda and C. A. Mattmann, Clustering Web Pages Based on Structure and Style Similarity (Application Paper), 2016 IEEE 17th International Conference on Information Reuse and Integration (IRI), Pittsburgh, PA, 2016, pp. 175-180. <http://ieeexplore.ieee.org/document/7785739/>`_

Development
===========

See `CONTRIBUTING.md` file
 

TODO
====

* [ ] Add information about the package in pypi
* [ ] Add documentation
* [ ] Add examples
