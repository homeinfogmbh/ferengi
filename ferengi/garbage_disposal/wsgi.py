"""WSGI interface."""

from hwdb import System
from wsgilib import JSON

from ferengi.garbage_disposal.orm import Location


__all__ = ['ROUTES']


def get_garbage_disposal(ident: int) -> JSON:
    """Returns garbage disposal information for the respective terminal."""

    try:
        system = System[ident]
    except System.DoesNotExist:
        return ('No such system.', 404)

    if system.deployment is None:
        return ('System is not deployed.', 400)

    locations = [
        location.to_json() for location in
        Location.by_address(system.deployment.address)]

    if not locations:
        return ('No garbage disposal information available.', 404)

    return JSON(locations)


ROUTES = [('GET', '/garbage-disposal/<int:ident>', get_garbage_disposal)]
