import lxml.html
from lxml.etree import _Element, _ElementTree


def label(el: _Element) -> str:
    if isinstance(el, lxml.html.HtmlComment):
        return 'comment'
    if isinstance(el, lxml.html.HtmlProcessingInstruction):
        return 'processing-instruction'
    if isinstance(el, lxml.html.HtmlElement):
        return el.tag
    raise ValueError('Don\'t know what to do with element: {}'.format(el))


def get_tags(doc: _ElementTree) -> list[str]:
    '''
    Get tags from a DOM tree

    :param doc: lxml parsed object
    :return:
    '''
    return [label(el) for el in doc.getroot().iter()]
