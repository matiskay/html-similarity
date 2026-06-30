__all__ = [
    'style_similarity',
    'structural_similarity',
    'similarity',
    'HtmlParsingError',
    'StructuralAlgorithm',
]


from html_similarity.exceptions import HtmlParsingError
from html_similarity.style_similarity import style_similarity
from html_similarity.structural_similarity import StructuralAlgorithm, structural_similarity
from html_similarity.similarity import similarity
