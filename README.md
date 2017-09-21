# HTML Similarity Tools

This package provides a set of functions to measure the similarity of two html pages.


## Recomendations for joint similarity

Using `k=0.3` give use better results. The style similarity can gives more information 
about the similarity rather than the style.


### Structural Similarity


### Style Similarity


### Joint Similarity (Structural Similarity and Style Similarity)

```
    k * structural_similarity(document_1, document_2) + (1 - k) * style_similarity(document_1, document_2)
```

Always the value is in the interval of 0 and 1.


## Inspiration

This is based on the job of [Clustering Web Pages Based on Structure and Style Similarity](http://ieeexplore.ieee.org/document/7785739/)
We are not using tree edit distance because it is quite slow compare to using diff.

## TODO

* [ ] Add tests
* [ ] Improve performance.

