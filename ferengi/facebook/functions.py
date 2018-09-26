"""Miscellaneous functions."""

from pathlib import Path
from urllib.parse import urlparse

from ferengi.facebook import dom


__all__ = ['encode_image_url', 'decode_image_url', 'posts_to_dom']


SCHEME = 'https'
HOST = 'ferengi.homeinfo.de'
IMG_PATH = Path('/facebook/image')


def encode_image_url(url, img_path=IMG_PATH):
    """Translates URLSs to be proxied."""

    url = urlparse(url)

    if url.params:
        raise ValueError('Cannot encode URL with params.')

    params = ';{}'.format(url.netloc)
    query = '?{}'.format(url.query) if url.query else ''
    return '{}://{}{}{}{}{}'.format(
        SCHEME, HOST, img_path, url.path, params, query)


def decode_image_url(url, img_path=IMG_PATH):
    """Translates URLSs to be proxied."""

    url = urlparse(url)
    path = Path(url.path)
    img_path = Path(IMG_PATH)
    offset = len(img_path.parts)
    parts = path.parts[offset:]
    path = '/' + '/'.join(parts)
    host = url.params
    query = '?{}'.format(url.query) if url.query else ''
    return '{}://{}{}{}'.format(SCHEME, host, path, query)


def posts_to_dom(posts, proxy=False):
    """Converts the given posts to XML dom."""

    channel = dom.channel()

    for post in posts:
        content = dom.Content()
        content.created_time = post.created
        content.from_ = post.author
        content.message = post.html

        if proxy:
            content.image = encode_image_url(post.image)
        else:
            content.image = post.image

        channel.content_.append(content)

    return channel
