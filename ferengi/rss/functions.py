"""Common functions."""

from timelib import RSS_DATETIME, strpdatetime


__all__ = ['strprssdatetime', 'strfrssdatetime']


def strprssdatetime(value):
    """Parses an RSS-formatted datetime value from a string."""

    return strpdatetime(value, formats=[RSS_DATETIME])


def strfrssdatetime(value):
    """Formats a datetime value into and RSS datetime string."""

    if value is None:
        return None

    return value.strftime(RSS_DATETIME)
