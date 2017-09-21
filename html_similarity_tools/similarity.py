from html_similarity_tools.style_similarity import style_similarity
from html_similarity_tools.structural_similarity import structural_similarity


def similarity(document_1, document_2, k=0.5):
    return k * structural_similarity(document_1, document_2) + (1 - k) * style_similarity(document_1, document_2)


