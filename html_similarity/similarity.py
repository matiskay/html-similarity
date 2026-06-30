from html_similarity.style_similarity import style_similarity
from html_similarity.structural_similarity import structural_similarity


def similarity(document_1: str, document_2: str, k: float = 0.5) -> float:
    return k * structural_similarity(document_1, document_2) + (1 - k) * style_similarity(document_1, document_2)
