"""WSGI interface."""

from terminallib import Terminal
from wsgilib import JSON

from ferengi.garbage_disposal.orm import Location


__all__ = ['ROUTES']


def get_garbage_disposal(terminal):
    """Returns garbage disposal information for the respective terminal."""

    try:
        tid, cid = terminal.split('.')
    except ValueError:
        return ('Invalid terminal ID.', 400)

    try:
        terminal = Terminal.by_ids(cid, tid)
    except Terminal.DoesNotExist:
        return ('No such terminal.', 404)

    if terminal.address is None:
        return ('Terminal is not located.', 400)

    locations = [
        location.to_dict() for location in
        Location.by_address(terminal.address)]

    if not locations:
        return ('No garbage disposal information available.', 404)

    return JSON(locations)


ROUTES = (
    ('GET', '/garbage-disposal/<terminal>', get_garbage_disposal,
     'get_garbage_disposal'),)
