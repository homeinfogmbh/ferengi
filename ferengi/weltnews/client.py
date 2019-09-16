"""HTTP client."""

from urllib.parse import urljoin

from ferengi.weltnews.orm import News


__all__ = ['urls', 'update']


BASE_URL = 'http://homeinfo.weltoohservice.de/xml/'
FILES = (
    'auto', 'karriere', 'kultur', 'leute', 'multimedia', 'olympia2018',
    'panorama', 'politik', 'reise', 'sport', 'test', 'wirtschaft', 'wissen',
    'wissenschaft', 'wm2018'
)


def urls(base_url=BASE_URL, files=FILES):
    """Yields complete URLs to XML files."""

    for file in files:
        yield urljoin(base_url, f'{file}.xml')


def update(base_url=BASE_URL, files=FILES):
    """Updates the records."""

    for url in urls(base_url=base_url, files=files):
        News.update_from_url(url)
