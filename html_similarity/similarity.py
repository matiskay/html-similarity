from html_similarity.algorithms import ALGORITHMS, DEFAULT_ALGORITHM, StructuralAlgorithm
from html_similarity.parsing import parse_html
from html_similarity.style_similarity import get_classes, jaccard_similarity


def similarity(
    document_1: str | bytes,
    document_2: str | bytes,
    k: float = 0.5,
    algorithm: StructuralAlgorithm | str = DEFAULT_ALGORITHM,
) -> float:
    """
    Computes a weighted combination of structural and style similarity.

    Each document is parsed once and the tree is shared between the
    structural and style scores.

    :param document_1: html string or bytes
    :param document_2: html string or bytes
    :param k: weight of the structural score; the style score gets ``1 - k``
    :param algorithm: structural comparison algorithm, see
        :class:`html_similarity.algorithms.StructuralAlgorithm`
    :return: Number between 0 and 1. If the number is next to 1 the pages are really similar.
    :raises HtmlParsingError: if either document cannot be parsed
    """
    algorithm = StructuralAlgorithm(algorithm)

    tree_1 = parse_html(document_1)
    tree_2 = parse_html(document_2)

    structural = ALGORITHMS[algorithm](tree_1, tree_2)
    style = jaccard_similarity(get_classes(tree_1), get_classes(tree_2))
    return k * structural + (1 - k) * style
