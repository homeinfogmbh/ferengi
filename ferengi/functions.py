"""Common functions."""

from typing import Iterable, Optional

from lxml.html import HtmlElement, document_fromstring
from requests import get

from filedb import File


__all__ = ['add_file_from_url', 'extract_text']


def add_file_from_url(url: str) -> File:
    """Downloads a file from the given URL
    and adds it to the filedb returning its ID.
    """

    return File.from_bytes(get(url).content)


def extract_text(string: str) -> str:
    """Extract text from a potential HTML string."""

    return extract_text_from_html_elements(
        document_fromstring(string).getchildren()
    )


def extract_text_from_html_elements(
        elements: Iterable[HtmlElement]
) -> Optional[str]:
    """Extract text from HTML elements."""

    children = []

    for element in elements:
        if text := element.text:
            return text

        children.extend(element.iterchildren())

    if children:
        return extract_text_from_html_elements(children)

    return None
