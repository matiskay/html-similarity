from collections import Counter

from lxml.etree import _Element, _ElementTree

from html_similarity.algorithms.common import label


def get_pq_grams(doc: _ElementTree, p: int = 2, q: int = 3) -> Counter[tuple[str, ...]]:
    '''
    Build the pq-gram profile of a DOM tree (Augsten, Bohlen & Gamper, 2005): a
    multiset of small ancestor x sibling label windows that approximates tree
    edit distance in roughly linear time, unlike a flat tag sequence which
    discards parent/child nesting.

    :param doc: lxml parsed object
    :param p: number of ancestor labels (incl. the node itself) per gram
    :param q: size of the sibling window per gram
    :return: multiset (Counter) of pq-grams
    '''
    grams: Counter[tuple[str, ...]] = Counter()
    star = '*'

    def visit(el: _Element, ancestors: tuple[str, ...]) -> None:
        node_label = label(el)
        children = list(el.iterchildren())

        if not children:
            grams[(node_label, *ancestors, *((star,) * q))] += 1
        else:
            child_labels = [label(c) for c in children]
            padded = [star] * (q - 1) + child_labels + [star] * (q - 1)
            for i in range(len(children) + q - 1):
                grams[(node_label, *ancestors, *padded[i:i + q])] += 1

        next_ancestors = (node_label, *ancestors)[:p - 1]
        for child in children:
            visit(child, next_ancestors)

    visit(doc.getroot(), (star,) * (p - 1))
    return grams


def similarity(tree_1: _ElementTree, tree_2: _ElementTree) -> float:
    '''
    Tree-structure aware comparison. Approximates Tree Edit Distance by
    comparing pq-gram profiles (Dice coefficient on the multiset intersection)
    instead of a flat sequence.
    '''
    grams_1 = get_pq_grams(tree_1)
    grams_2 = get_pq_grams(tree_2)
    total = sum(grams_1.values()) + sum(grams_2.values())
    if total == 0:
        return 1.0
    common = sum((grams_1 & grams_2).values())
    return 2 * common / total
