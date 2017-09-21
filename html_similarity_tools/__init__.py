from html_similarity_tools.style_similarity import style_similarity
from html_similarity_tools.structural_similarity import structural_similarity
from html_similarity_tools.similarity import similarity

import pkgutil

__version__ = pkgutil.get_data(__package__, 'VERSION').decode('ascii').strip()
version_info = tuple(int(v) if v.isdigit() else v for v in __version__.split('.'))

del pkgutil