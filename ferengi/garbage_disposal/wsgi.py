"""WSGI interface."""

from hwdb import System
from wsgilib import JSON

from ferengi.garbage_disposal.orm import Location


__all__ = ['ROUTES']


def for_system(ident: int) -> JSON:
    """Returns garbage disposal information for the respective system."""

    try:
        system = System.select(cascade=True).where(System.id == ident).get()
    except System.DoesNotExist:
        return ('No such system.', 404)

    if system.deployment is None:
        return ('System is not deployed.', 400)

    locations = [
        location.to_json() for location in
        Location.by_address(system.deployment.address)
    ]

    if not locations:
        return ('No garbage disposal information available.', 404)

    return JSON(locations)


ROUTES = [('GET', '/garbage-disposal/<int:ident>', for_system)]
