"""Miscellaneous functions."""

from ferengi.facebook import dom

__all__ = ['posts_to_dom']


def posts_to_dom(posts):
    """Converts the given posts to XML dom."""

    channel = dom.channel()

    for post in posts:
        content = dom.Content()
        content.created_time = post.created
        content.from_ = post.author
        content.message = post.html
        content.image = post.image
        channel.content.append(content)

    return channel
